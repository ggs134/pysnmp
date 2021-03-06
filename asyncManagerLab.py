from pysnmp.entity.rfc3413.oneliner import cmdgen

import requests
import time
import pymongo

mongoClient = pymongo.MongoClient("52.78.93.195",27017)
etcCollection = mongoClient["MiningPoolHub"]["etc"]
ethCollection = mongoClient["MiningPoolHub"]["eth"]

data = ethCollection.find(sort=[("_id",-1)]).limit(1).next()["data"][0]
dataC = etcCollection.find(sort=[("_id",-1)]).limit(1).next()["data"][0]

addrList = {10:"192.168.1.8" ,11:"192.168.1.3", 12:"192.168.1.7", 14:"192.168.1.5"}

# response = requests.get("http://ethereum.miningpoolhub.com/index.php?page=api&action=getuserworkers&api_key=a8c9f5ea1a4045f6809c9a47c4746f5ae4aa5e136bf96ec0ce4223734c96a128")
# json_response = response.json()
# data = json_response["getuserworkers"]["data"]
#
# response2 = requests.get("http://ethereum-classic.miningpoolhub.com/index.php?page=api&action=getuserworkers&api_key=a8c9f5ea1a4045f6809c9a47c4746f5ae4aa5e136bf96ec0ce4223734c96a128")
# json_response2 = response2.json()
# dataC = json_response2["getuserworkers"]["data"]

#mongo client
cli = pymongo.MongoClient('52.78.93.195', 27017)
db = cli['di']

# mak2addr = "goldrush.iptime.org"
# mak1addr = "222.98.97.238"

# smiSet = ( cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,i,0).addAsn1MibSource('./') for i in range(2,44) )

smiSet = ( cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,2,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,3,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,4,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,5,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,6,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,7,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,8,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,9,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,10,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,11,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,12,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,13,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,14,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,15,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,16,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,17,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,18,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,19,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,20,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,21,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,22,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,23,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,24,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,25,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,26,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,27,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,28,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,29,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,30,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,31,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,32,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,33,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,34,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,35,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,36,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,37,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,38,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,39,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,40,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,41,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,42,0).addAsn1MibSource('./'),
  cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,43,0).addAsn1MibSource('./'),)




# List of targets in the followin format:
# ( ( authData, transportTarget, varNames ), ... )

targets = (( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
  cmdgen.UdpTransportTarget((addrList[i], 161)),smiSet ) for i in addrList)

# targets = (
#     # miner1 target (SNMPv3 over IPv4/UDP)
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#       cmdgen.UdpTransportTarget((mak1addr, 60001)),smiSet ),
#     #miner3
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#       cmdgen.UdpTransportTarget((mak1addr, 60003)),smiSet ),
#     #miner4
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#       cmdgen.UdpTransportTarget((mak1addr, 60004)),smiSet ),
#      #miner5
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak1addr, 60005)),smiSet ),
#     #miner6
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak1addr, 60006)),smiSet ),
#     #miner8
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak1addr, 60008)),smiSet ),
#     # #miner14
#     # ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#     #     cmdgen.UdpTransportTarget((mak1addr, 60014)),smiSet ),
#     #miner15
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60015)),smiSet ),
#     #miner16
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60016)),smiSet ),
#     #miner17
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60017)),smiSet ),
#     #miner18
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60018)),smiSet ),
#     #miner19
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60019)),smiSet ),
#     #miner20
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60020)),smiSet ),
#     #miner21
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60021)),smiSet ),
#     #miner22
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60022)),smiSet ),
#     #miner23
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60023)),smiSet ),
#     #miner24
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60024)),smiSet ),
#     #miner25
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60025)),smiSet ),
#     #miner26
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60026)),smiSet ),
#     #miner27
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60027)),smiSet ),
#     #miner28
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60028)),smiSet ),
#     #miner29
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60029)),smiSet ),
#     #miner30
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60030)),smiSet ),
#     #miner31
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60031)),smiSet ),
#     #miner32
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60032)),smiSet ),
#     #miner33
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60033)),smiSet ),
#     #miner34
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60034)),smiSet ),
#     #miner35
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60035)),smiSet ),
#     #miner36
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60036)),smiSet ),
#     #miner38
#     ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
#         cmdgen.UdpTransportTarget((mak2addr, 60038)),smiSet ),
# )

# Wait for responses or errors
def cbFun(sendRequestHandle, errorIndication, errorStatus, errorIndex, varBinds, cbCtx):
    (authData, transportTarget) = cbCtx
    # print('%s via %s' % (authData, transportTarget))
    result = {}
    count = 0
    keys = ['username','gpuTemperature', 'gpuLoad', 'coreClock', 'cpuPercent', 'virtualTotal', 'virtualAvailable',
    'virtualPercent', 'virtualUsed','virtualFree','virtualActive','virtualInactive','bytesSent','bytesRecv',
    'packetsSent', 'packetsRecv', 'errin', 'errout', 'dropIn', 'dropOut', 'bootTime', 'ethminerStatus',
    'ethminerCPUPercent', 'ethminerMemoryPercent', 'ethminerRss', 'ethminerVms', 'ethminerShared', 'ethminerText',
    'ethminerLib', 'ethminerData', 'ethminerDirty', 'ethminerUss', 'ethminerPss', 'ethminerSwap',
    'ethminerReadCount', 'ethminerWriteCount', 'ethminerReadBytes', 'ethminerWriteBytes', 'ethminerNumThreads',
    'ethminerCTXVolSwitches', 'ethminerCTXInvloSwitches','fanspeed']
    if errorIndication:
        print(errorIndication)
        print('%s via %s' % (authData, transportTarget))
        return 1
    if errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1] or '?'
            )
        )
        return 1

    for oid, val in varBinds:
        if val is None:
            # print(oid.prettyPrint())
            result[keys[count]]=val.prettyPrint()
            count += 1
        else:
            # print('%s = %s' % (oid.prettyPrint(), val.prettyPrint()))
            result[keys[count]]=val.prettyPrint()
            count += 1
    # if result != []:

    for i in data:
        if result["username"] in i["username"]:
            result["hashrate"] = i["hashrate"]
    for j in dataC:
        if result["username"] in j["username"]:
            result["hashrateC"] = j["hashrate"]
    result["time"] = time.time()

    # print result
    db[result["username"]].insert(result)

cmdGen  = cmdgen.AsynCommandGenerator()

# Submit GET requests

# result = []
for authData, transportTarget, varNames in targets:
    cmdGen.getCmd(
        authData, transportTarget, varNames,
        # User-space callback function and its context
        (cbFun, (authData, transportTarget)),
        lookupNames=True, lookupValues=True
    )
# print result

cmdGen.snmpEngine.transportDispatcher.runDispatcher()
