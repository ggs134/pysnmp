from pysnmp.entity.rfc3413.oneliner import cmdgen

# List of targets in the followin format:
# ( ( authData, transportTarget, varNames ), ... )
targets = (
    # 1-st target (SNMPv3 over IPv4/UDP)
    ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
      cmdgen.UdpTransportTarget(('192.168.0.39', 161)),
      ( cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,2,0).addAsn1MibSource('./'),
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
        cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,43,0).addAsn1MibSource('./'),) ),
    # 2-st target (SNMPv3 over IPv4/UDP)
    ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
      cmdgen.UdpTransportTarget(('192.168.0.36', 161)),
      ( cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,2,0).addAsn1MibSource('./'),
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
        cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,43,0).addAsn1MibSource('./'),) ),
    # # 3-st target (SNMPv3 over IPv4/UDP)
    # ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
    #   cmdgen.UdpTransportTarget(('onther.iptime.org', 60004)),
    #   ( cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,2,0).addAsn1MibSource('./'),
    #     cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,1,0).addAsn1MibSource('./') ) ),
    # # 4-st target (SNMPv1 over IPv4/UDP)
    # ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
    #   cmdgen.UdpTransportTarget(('onther.iptime.org', 60005)),
    #   ( cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,2,0).addAsn1MibSource('./'),
    #     cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,1,0).addAsn1MibSource('./') ) ),
    #
    # # 5-st target (SNMPv1 over IPv4/UDP)
    # ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
    #   cmdgen.UdpTransportTarget(('onther.iptime.org', 60006)),
    #   ( cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,2,0).addAsn1MibSource('./'),
    #     cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,1,0).addAsn1MibSource('./') ) ),
    # # 6-st target (SNMPv1 over IPv4/UDP)
    # ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
    #   cmdgen.UdpTransportTarget(('onther.iptime.org', 60007)),
    #   ( cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,2,0).addAsn1MibSource('./'),
    #     cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,1,0).addAsn1MibSource('./') ) ),
    # # 7-st target (SNMPv1 over IPv4/UDP)
    # ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
    #   cmdgen.UdpTransportTarget(('onther.iptime.org', 60008)),
    #   ( cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,2,0).addAsn1MibSource('./'),
    #     cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,1,0).addAsn1MibSource('./') ) ),
)

# Wait for responses or errors
def cbFun(sendRequestHandle, errorIndication, errorStatus, errorIndex, varBinds, cbCtx):
    (authData, transportTarget) = cbCtx
    # print('%s via %s' % (authData, transportTarget))
    result = {}
    count = 0
    keys = ['username','gpuTemperature', 'gpuLoad', 'coreClock', 'memoryClock', 'cpuPercent', 'virtualTotal', 'virtualAvailable',
    'virtualPercent', 'virtualUsed','virtualFree','virtualActive','virtualInactive','bytesSent','bytesRecv',
    'packetsSent', 'packetsRecv', 'errin', 'errout', 'dropIn', 'dropOut', 'bootTime', 'ethminerStatus',
    'ethminerCPUPercent', 'ethminerMemoryPercent', 'ethminerRss', 'ethminerVms', 'ethminerShared', 'ethminerText',
    'ethminerLib', 'ethminerData', 'ethminerDirty', 'ethminerUss', 'ethminerPss', 'ethminerSwap',
    'ethminerReadCount', 'ethminerWriteCount', 'ethminerReadBytes', 'ethminerWriteBytes', 'ethminerNumThreads',
    'ethminerCTXVolSwitches', 'ethminerCTXInvloSwitches']
    if errorIndication:
        print(errorIndication)
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
            print(oid.prettyPrint())
            result.update(keys[count]=val.prettyPrint())
            count += 1
        else:
            print('%s = %s' % (oid.prettyPrint(), val.prettyPrint()))
            result.update(keys[count]=val.prettyPrint())
            count += 1
    # if result != []:
    print result

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
