from pysnmp.entity.rfc3413.oneliner import cmdgen

# List of targets in the followin format:
# ( ( authData, transportTarget, varNames ), ... )
targets = (
    # 1-st target (SNMPv3 over IPv4/UDP)
    ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
      cmdgen.UdpTransportTarget(('192.168.0.39', 161)),
      ( cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,2,0).addAsn1MibSource('./'),
        cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,1,0).addAsn1MibSource('./') ) ),
    # 2-st target (SNMPv3 over IPv4/UDP)
    ( cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
      cmdgen.UdpTransportTarget(('192.168.0.36', 161)),
      ( cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,2,0).addAsn1MibSource('./'),
        cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,1,0).addAsn1MibSource('./') ) ),
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
    result = []
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
        else:
            print('%s = %s' % (oid.prettyPrint(), val.prettyPrint()))
            result.append(val.prettyPrint())
    if result != []:
        print result

cmdGen  = cmdgen.AsynCommandGenerator()

# Submit GET requests

result = []
for authData, transportTarget, varNames in targets:
    cmdGen.getCmd(
        authData, transportTarget, varNames,
        # User-space callback function and its context
        (cbFun, (authData, transportTarget)),
        lookupNames=True, lookupValues=True
    )
print result

cmdGen.snmpEngine.transportDispatcher.runDispatcher()
