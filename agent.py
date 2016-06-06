from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.carrier.asynsock.dgram import udp
from pysnmp.smi import builder

import threading
import collections
import time
import sys
import os
import json

import readGPUTemp

filepath = os.path.dirname(os.path.realpath(__file__))

MibObject = collections.namedtuple('MibObject', ['mibName','objectType', 'valueGetFunc'])

with open(filepath+"/setting.txt") as settings:
    _json_obj = json.loads(settings)
    _addr = _json_obj["address"]
    _port = _json_obj["port"]
    _account = _json_obj["id"]
    _auth_key = _json_obj['auth_key']
    _priv_key = _json_obj['priv_key']

class CustomMib(object):
#=====================================================================================
    def __init__(self, path):
        self._lock = threading.RLock()
        self._hashrate = 0
        self._file_path = path
    #=====================================================================================
    def getDescription(self):
        res = readGPUTemp.parseResult()
        return res
    #=====================================================================================
    def getHashrate(self):
        with self._lock:
    # self._hashrate = self._getHash()
            return self._getHash()

    def _getHash(self):
        with open(self._file_path) as f:
            lines = f.readlines()
            last = lines[-1]
            split = last.split()

            # if len(split)<7:
            #     res = 10
            #
            # elif split[2].startswith("Mining"):
            #     res = 10
            #
            # else:
            #     res = int(split[7])
            try:
                res = int(split[7])
            except Exception as e:
                res = 10
    # print res
            return res

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

cmib = CustomMib(str(sys.argv[1]))
objects = [MibObject('MY-MIB', 'hashrateDescription', cmib.getDescription), MibObject('MY-MIB', 'hashrate', cmib.getHashrate)]



snmpEngine = engine.SnmpEngine()

config.addSocketTransport( snmpEngine, udp.domainName, udp.UdpTransport().openServerMode((_addr, _port)))
config.addV3User(snmpEngine,_account,config.usmHMACMD5AuthProtocol,_auth_key,config.usmDESPrivProtocol,_priv_key)
config.addVacmUser(snmpEngine, 3, _account, _priv_key,(1,3,6,1,4,1), (1,3,6,1,4,1))

snmpContext = context.SnmpContext(snmpEngine)


#builder create
mibBuilder = snmpContext.getMibInstrum().getMibBuilder()
mibSources = mibBuilder.getMibSources() + (builder.DirMibSource('.'),)+(builder.DirMibSource(filepath),)
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
