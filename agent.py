from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.carrier.asynsock.dgram import udp
from pysnmp.smi import builder

from getData import DataHouse

import threading
import collections
import time
import sys
import os
import json

filepath = os.path.dirname(os.path.realpath(__file__))

MibObject = collections.namedtuple('MibObject', ['mibName','objectType', 'valueGetFunc'])

with open(filepath+"/settings.txt") as settings:
    _json_obj = json.loads(settings.read())
    _addr = _json_obj["address"]
    _port = _json_obj["port"]
    _account = _json_obj["id"]
    _auth_key = _json_obj['auth_key']
    _priv_key = _json_obj['priv_key']

class CustomMib(object):
#=====================================================================================
    def __init__(self):
        self._lock = threading.RLock()
        self._house = DataHouse()
        self._virtual = self._house.virtualMemory
        self._network = self._house.networkUsage
        self._ethminer = self._house.ethminerProcess.as_dict()
    #=====================================================================================
    def getUsername(self):
        return self._ethminer["username"]
    #=====================================================================================
    def getHashrate(self):
        with self._lock:
    # self._hashrate = self._getHash()
            return 0
    def getGpuTemprature(self):
        with self._lock:
            return self._house.temperature
    def getGpuLoad(self):
        with self._lock:
            return str(self._house.gpuLoad)
    def getCoreClock(self):
        with self._lock:
            return str(self._house.coreClock)
    def getMemoryClock(self):
        with self._lock:
            return str(self._house.memoryClock)
    def getCpuPercent(self):
        with self._lock:
            return str(self._house.cpuPercent)
    def getVirtualTotal(self):
        with self._lock:
            return str(self._virtual.total)
    def getVirtualAvailable(self):
        with self._lock:
            return str(self._virtual.available)
    def getVirtualPercent(self):
        with self._lock:
            return str(self._virtual.percent)
    def getVirtualUsed(self):
        with self._lock:
            return str(self._virtual.used)
    def getVirtualFree(self):
        with self._lock:
            return str(self._virtual.free)
    def getVirtualActive(self):
        with self._lock:
            return str(self._virtual.active)
    def getVirtualInactive(self):
        with self._lock:
            return str(self._virtual.inactive)
    def getBytesSent(self):
        with self._lock:
            return str(self._network.bytes_sent)
    def getBytesRecv(self):
        with self._lock:
            return str(self._network.bytes_recv)
    def getPacketsSent(self):
        with self._lock:
            return str(self._network.packets_sent)
    def getPacketsRecv(self):
        with self._lock:
            return str(self._network.packets_recv)
    def getErrin(self):
        with self._lock:
            return str(self._network.errin)
    def getErrout(self):
        with self._lock:
            return str(self._network.errout)
    def getDropIn(self):
        with self._lock:
            return str(self._network.dropin)
    def getDropOut(self):
        with self._lock:
            return str(self._network.dropout)
    def getBootTime(self):
        with self._lock:
            return str(self._house.bootTime)
    def getEthminerStatus(self):
        with self._lock:
            return str(self._ethminer["status"])
    def getEthminerCPUPercent(self):
        with self._lock:
            return str(self._ethminer["cpu_percent"])
    def getEthminerMemoryPercent(self):
        with self._lock:
            return str(self._ethminer["memory_percent"])
    def getEthminerRss(self):
        with self._lock:
            return str(self._ethminer["memory_info"].rss)
    def getEthminerVms(self):
        with self._lock:
            return str(self._ethminer["memory_info"].vms)
    def getEthminerShared(self):
        with self._lock:
            return str(self._ethminer["memory_info"].shared)
    def getEthminerText(self):
        with self._lock:
            return str(self._ethminer["memory_info"].text)
    def getEthminerLib(self):
        with self._lock:
            return str(self._ethminer["memory_info"].lib)
    def getEthminerData(self):
        with self._lock:
            return str(self._ethminer["memory_info"].data)
    def getEthminerDirty(self):
        with self._lock:
            return str(self._ethminer["memory_info"].dirty)
    def getEthminerUss(self):
        with self._lock:
            return str(self._ethminer["memory_full_info"].uss)
    def getEthminerPss(self):
        with self._lock:
            return str(self._ethminer["memory_full_info"].pss)
    def getEthminerSwap(self):
        with self._lock:
            return str(self._ethminer["memory_full_info"].swap)
    def getEthminerReadCount(self):
        with self._lock:
            return str(self._ethminer["io_counters"].read_count)
    def getEthminerWriteCount(self):
        with self._lock:
            return str(self._ethminer["io_counters"].write_count)
    def getEthminerReadBytes(self):
        with self._lock:
            return str(self._ethminer["io_counters"].read_bytes)
    def getEthminerWriteBytes(self):
        with self._lock:
            return str(self._ethminer["io_counters"].write_bytes)
    def getEthminerNumThreads(self):
        with self._lock:
            return str(self._ethminer["num_threads"])
    def getEthminerCTXVolSwitches(self):
        with self._lock:
            return str(self._ethminer['num_ctx_switches'].voluntary)
    def getEthminerCTXInvloSwitches(self):
        with self._lock:
            return str(self._ethminer['num_ctx_switches'].involuntary)


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

cmib = CustomMib()
objects =[]
objects.append(MibObject('MY-MIB', 'hashrateDescription', cmib.getDescription))
objects.append(MibObject('MY-MIB', 'username', cmib.getUsername))
objects.append(MibObject('MY-MIB', 'gpuTemperature', cmib.getGpuTemprature))
objects.append(MibObject('MY-MIB', 'gpuLoad', cmib.getGpuLoad))
objects.append(MibObject('MY-MIB', 'coreClock', cmib.getCoreClock))
objects.append(MibObject('MY-MIB', 'cpuPercent', cmib.getCpuPercent))
objects.append(MibObject('MY-MIB', 'virtualTotal', cmib.getVirtualTotal))
objects.append(MibObject('MY-MIB', 'virtualAvailable', cmib.getVirtualAvailable))
objects.append(MibObject('MY-MIB', 'virtualPercent', cmib.getVirtualPercent))
objects.append(MibObject('MY-MIB', 'virtualUsed', cmib.getVirtualUsed))
objects.append(MibObject('MY-MIB', 'virtualFree', cmib.getVirtualFree))
objects.append(MibObject('MY-MIB', 'virtualActive', cmib.getVirtualActive))
objects.append(MibObject('MY-MIB', 'virtualInactive', cmib.getVirtualInactive))
objects.append(MibObject('MY-MIB', 'bytesSent', cmib.getBytesSent))
objects.append(MibObject('MY-MIB', 'bytesRecv', cmib.getBytesRecv))
objects.append(MibObject('MY-MIB', 'packetsSent', cmib.getPacketsSent))
objects.append(MibObject('MY-MIB', 'packetsRecv', cmib.getPacketsRecv))
objects.append(MibObject('MY-MIB', 'errin', cmib.getErrin))
objects.append(MibObject('MY-MIB', 'errout', cmib.getErrout))
objects.append(MibObject('MY-MIB', 'dropIn', cmib.getDropIn))
objects.append(MibObject('MY-MIB', 'dropOut', cmib.getDropOut))
objects.append(MibObject('MY-MIB', 'bootTime', cmib.getBootTime))
objects.append(MibObject('MY-MIB', 'ethminerStatus', cmib.getEthminerStatus))
objects.append(MibObject('MY-MIB', 'ethminerCPUPercent', cmib.getEthminerCPUPercent))
objects.append(MibObject('MY-MIB', 'ethminerMemoryPercent', cmib.getEthminerMemoryPercent))
objects.append(MibObject('MY-MIB', 'ethminerRss', cmib.getEthminerRss))
objects.append(MibObject('MY-MIB', 'ethminerVms', cmib.getEthminerVms))
objects.append(MibObject('MY-MIB', 'ethminerShared', cmib.getEthminerShared))
objects.append(MibObject('MY-MIB', 'ethminerText', cmib.getEthminerText))
objects.append(MibObject('MY-MIB', 'ethminerLib', cmib.getEthminerLib))
objects.append(MibObject('MY-MIB', 'ethminerData', cmib.getEthminerData))
objects.append(MibObject('MY-MIB', 'ethminerDirty', cmib.getEthminerDirty))
objects.append(MibObject('MY-MIB', 'ethminerUss', cmib.getEthminerUss))
objects.append(MibObject('MY-MIB', 'ethminerPss', cmib.getEthminerPss))
objects.append(MibObject('MY-MIB', 'ethminerSwap', cmib.getEthminerSwap))
objects.append(MibObject('MY-MIB', 'ethminerReadCount', cmib.getEthminerReadCount))
objects.append(MibObject('MY-MIB', 'ethminerWriteCount', cmib.getEthminerWriteCount))
objects.append(MibObject('MY-MIB', 'ethminerReadBytes', cmib.getEthminerReadBytes))
objects.append(MibObject('MY-MIB', 'ethminerWriteBytes', cmib.getEthminerWriteBytes))
objects.append(MibObject('MY-MIB', 'ethminerNumThreads', cmib.getEthminerNumThreads))
objects.append(MibObject('MY-MIB', 'ethminerCTXVolSwitches', cmib.getEthminerCTXVolSwitches))
objects.append(MibObject('MY-MIB', 'ethminerCTXInvolSwitches', cmib.getEthminerCTXInvloSwitches))


snmpEngine = engine.SnmpEngine()

config.addSocketTransport( snmpEngine, udp.domainName, udp.UdpTransport().openServerMode((_addr, _port)))
config.addV3User(snmpEngine,_account,config.usmHMACMD5AuthProtocol,_auth_key,config.usmDESPrivProtocol,_priv_key)
config.addVacmUser(snmpEngine, 3, _account, "authPriv",(1,3,6,1,4,1), (1,3,6,1,4,1))

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
