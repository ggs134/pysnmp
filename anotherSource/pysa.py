from pysnmp.entity import engine, config
from pysnmp import debug
from pysnmp.entity.rfc3413 import cmdrsp, context, ntforg
from pysnmp.carrier.asynsock.dgram import udp
from pysnmp.smi import builder

import threading
import collections
import time

MibObject = collections.namedtuple("MibObject", [ 'mibName','objectType','valueGetFunc','valueSetFunc' ])

class CustomMib(object):
  def __init__(self):
    self._lock = threading.RLock()
    self._test_count = 0
  
  def getTestDescription(self):
    return "My descrip {}".format(self._test_count)
  
  def getTestCount(self):
    with self._lock:
      return self._test_count

  def setTestCount(self, value):
    with self._lock:
      self._test_count = value

def createVariable(SuperClass, getValue, setValue,*args):
  
  class Var(SuperClass):
    def readGet(self, name, *args):
      return name, self.syntax.clone(getValue())
    def writeTest(self, name, val, *args):
      pass
    def writeCommit(self, name, val, *args):
      setValue(val)

  return Var(*args)

class SNMPAgent(object):
  def __init__(self, mibObjects):
    self._snmpEngine = engine.SnmpEngine()
    config.addSocketTransport(self._snmpEngine, udp.domainName, udp.UdpTransport().openServerMode(('',165)))
    config.addV1System(self._snmpEngine,"my-read-area","public")
    config.addV1System(self._snmpEngine,"my-write-area","private")
    config.addVacmUser(self._snmpEngine, 2,"my-read-area",'noAuthNoPriv',readSubTree=(1,3,6,1,4,1))
    config.addVacmUser(self._snmpEngine, 2,"my-write-area",'noAuthNoPriv',readSubTree=(1,3,6,1,4,1), writeSubTree=(1,3,6,1,4,1))
    self._snmpContext = context.SnmpContext(self._snmpEngine)

    mibBuilder = self._snmpContext.getMibInstrum().getMibBuilder()
    mibSources = mibBuilder.getMibSources()+(builder.DirMibSource('.'),)+(builder.DirMibSource('./pysnmp_mibs'),)
    mibBuilder.setMibSources(*mibSources)

    MibScalarInstance, = mibBuilder.importSymbols('SNMPv2-SMI','MibScalarInstance')
    for mibObject in mibObjects:
      nextVar, = mibBuilder.importSymbols(mibObject.mibName, mibObject.objectType)
      instance = createVariable(MibScalarInstance, mibObject.valueGetFunc, mibObject.valueSetFunc, nextVar.name, (0,), nextVar.syntax)
      instanceDict ={ str(nextVar.name)+"Instance":instance }
      mibBuilder.exportSymbols(mibObject.mibName, **instanceDict)

    cmdrsp.GetCommandResponder(self._snmpEngine, self._snmpContext)
    cmdrsp.NextCommandResponder(self._snmpEngine, self._snmpContext)
    cmdrsp.BulkCommandResponder(self._snmpEngine, self._snmpContext)

  def setTrapReceiver(self, host, community):
    config.addV1System(self._snmpEngine, 'nms-area',community)
    config.addVacmUser(self._snmpEngine, 2, 'nms-area','noAuthNoPriv', notifySubTree=(1,3,6,1,4,1))
    config.addTargetParams(self._snmpEngine, 'nms-creds', 'nms-area','noAuthNoPriv',1)
    config.addTargetAddr(self._snmpEngine, 'my-nms', udp.domainName, (host, 162), 'nms-creds',tagList = 'all-my-managers')
    config.addNotificationTarget(self._snmpEngine, 'test-notification', 'my-filter', 'all-my-managers', 'trap')
    
  def sendTrap(self):
    print "Sending Trap"
    ntfOrg = ntforg.NotificationOriginator(self._snmpContext)
    errorIndication = ntfOrg.sendNotification(self._snmpEngine, 'test-notification', ("MY-MIB", 'testTrap'), ())

  def serverForever(self):
    print "Starting agent"
    self._snmpEngine.transportDispatcher.jobStarted(1)
    try:
      self._snmpEngine.transportDispatcher.runDispatcher()
    except:
      self._snmpEngine.transportDispatcher.closeDispatcher()
      raise


class Worker(threading.Thread):
  def __init__(self, agent, mib):
    threading.Thread.__init__(self)
    self._agent = agent
    self._mib = mib
    self.setDaemon(True)
  def run(self):
    while True:
      time.sleep(3)
      customMib.setTestCount(customMib.getTestCount()+1)
      agent.sendTrap()

if __name__=="__main__":
  customMib = CustomMib()
  #objects = [MibObject('MY-MIB', 'testDescription', customMib.getTestDescription,''), MibObject('MY-MIB', 'testCount', customMib.getTestCount,'')]
  objects = [MibObject('MY-MIB', 'testDescription', customMib.getTestDescription, ''),MibObject('MY-MIB', 'testCount',customMib.getTestCount, customMib.setTestCount),]
  #MibObject('MY-MIB', 'ledControl', customMib.getTestCount, '')]
  agent = SNMPAgent(objects)
  agent.setTrapReceiver('172.0.0.1', 'traps')
  Worker(agent, customMib).start()
  try:
    agent.serverForever()
  except keyboardInterrupt:
    print "Shutting Down"
