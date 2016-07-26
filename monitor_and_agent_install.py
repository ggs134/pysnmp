import json
import os

filepath = os.path.dirname(os.path.realpath(__file__))

with open("/etc/supervisor/conf.d/monitor.conf", 'w') as mFile:
    mFile.write("[program:monitor]\n")
    mFile.write("command="+filepath+"/monitor.sh\n")
    mFile.write("autostart=true\n")
    mFile.write("stdout_logfile="+os.environ["HOME"]+"/log/monitor.out.log\n")
    mFile.write("stderr_logfile="+os.environ["HOME"]+"/log/monitor.err.log\n")
    mFile.write("user=root\n")

with open("/etc/supervisor/conf.d/agent.conf", 'w') as mFile:
    mFile.write("[program:agent]\n")
    mFile.write("command=python"+" "+filepath+"/agent.py"+"\n")
    mFile.write("autostart=true\n")
    mFile.write("autorestart=true\n")
    mFile.write("startretries=3\n")
    mFile.write("stdout_logfile="+os.environ["HOME"]+"/log/agent.out.log\n")
    mFile.write("stderr_logfile="+os.environ["HOME"]+"/log/agent.err.log\n")
    mFile.write("user=root\n")
