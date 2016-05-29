from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.carrier.asynsock.dgram import udp
from pysnmp.smi import builder

import threading
import collections
import time

MibObject = collections.namedtuple('MibObject', ['mibName','objectType', 'valueGetFunc'])

class CustomMib(object):
	"""Stores the data we want to serve.
	"""
	#=====================================================================================
	def __init__(self, num):
		self._lock = threading.RLock()
		self._test_count = num
	#=====================================================================================
	def getTestDescription(self):
		return "My Description [%s]" % self._test_count
	#=====================================================================================
	def getTestCount(self):
		with self._lock:
			return self._test_count
	# #=====================================================================================
	# def setTestCount(self, value):
	# 	with self._lock:
	# 		self._test_count = value


# def createVariable(SuperClass, getValue, setValue, *args):
def createVariable(SuperClass, getValue, *args):
	"""This is going to create a instance variable that we can export.
	getValue is a function to call to retreive the value of the scalar
	"""
	#=====================================================================================
	class Var(SuperClass):
		def readGet(self, name, *args):
			#print "	Getting var..."
			return name, self.syntax.clone(getValue())
		# #=====================================================================================
		# def writeTest(self, name, *args ):
		# 	#print " Testing var..."
		# 	pass
		# #=====================================================================================
		# def writeCommit(self, name, val, *args ):
		# 	#print " Setting var..."
		# 	setValue(val)
	return Var(*args)


#amin code

cmib = CustomMib(5717)
objects = [MibObject('MY-MIB', 'testDescription', cmib.getTestDescription), MibObject('MY-MIB', 'testCount', cmib.getTestCount)]



snmpEngine = engine.SnmpEngine()

config.addSocketTransport( snmpEngine, udp.domainName, udp.UdpTransport().openServerMode(('127.0.0.1', 161)))
config.addV3User(snmpEngine,'usr-md5-des',config.usmHMACMD5AuthProtocol,'authkey1',config.usmDESPrivProtocol,'privkey1')
config.addVacmUser(snmpEngine, 3, 'usr-md5-des', 'authPriv',(1,3,6,1,4,1), (1,3,6,1,4,1))

snmpContext = context.SnmpContext(snmpEngine)


#builder create
mibBuilder = snmpContext.getMibInstrum().getMibBuilder()
mibSources = mibBuilder.getMibSources() + (builder.DirMibSource('.'),)
mibBuilder.setMibSources(*mibSources)


MibScalarInstance, = mibBuilder.importSymbols('SNMPv2-SMI','MibScalarInstance')

for mibObject in objects:
    nextVar, = mibBuilder.importSymbols(mibObject.mibName,
                                        mibObject.objectType)
    instance = createVariable(MibScalarInstance, mibObject.valueGetFunc, nextVar.name, (0,),  nextVar.syntax)
    #need to export as <var name>Instance
    instanceDict = {str(nextVar.name)+"Instance":instance}
    mibBuilder.exportSymbols(mibObject.mibName, **instanceDict)

cmdrsp.GetCommandResponder(snmpEngine, snmpContext)
cmdrsp.SetCommandResponder(snmpEngine, snmpContext)
cmdrsp.NextCommandResponder(snmpEngine, snmpContext)
cmdrsp.BulkCommandResponder(snmpEngine, snmpContext)

# Register an imaginary never-ending job to keep I/O dispatcher running forever
snmpEngine.transportDispatcher.jobStarted(1)




# Run I/O dispatcher which would receive queries and send responses
try:
    snmpEngine.transportDispatcher.runDispatcher()
except:
    snmpEngine.transportDispatcher.closeDispatcher()
    raise
