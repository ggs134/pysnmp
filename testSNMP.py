from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.carrier.asynsock.dgram import udp

snmpEngine = engine.SnmpEngine()

config.addSocketTransport( snmpEngine, udp.domainName, udp.UdpTransport().openServerMode(('127.0.0.1', 161)))
config.addV3User(snmpEngine,'usr-md5-des',config.usmHMACMD5AuthProtocol,'authkey1',config.usmDESPrivProtocol,'privkey1')
config.addVacmUser(snmpEngine, 3, 'usr-md5-des', 'authPriv',(1,3,6,1,2,1), (1,3,6,1,2,1))

snmpContext = context.SnmpContext(snmpEngine)

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
