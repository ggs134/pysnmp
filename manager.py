
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.UsmUserData('goldrush', authKey="authkey1", privKey="privkey1", authProtocol=cmdgen.usmHMACMD5AuthProtocol, privProtocol=cmdgen.usmDESPrivProtocol),
    cmdgen.UdpTransportTarget(('192.168.0.39', 161)),
    cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,2,0).addAsn1MibSource('./'),
    cmdgen.MibVariable('SNMPv2-SMI', 'enterprises',42,1,0).addAsn1MibSource('./')
)

# Check for errors and print out results
if errorIndication:
    print "hello"
    print(errorIndication)
else:
    if errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1] or '?'
            )
        )
    else:
        for name, val in varBinds:
            print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
        #0 if no problem
        print(errorStatus)
        #None if no problem
        print(errorIndication)
