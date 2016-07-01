import subprocess
import os

class dataHouse:
    def __init__(self):
        pass

    def bashCommand(cmd, grep):
        p = subprocess.Popen(['/bin/bash', os.path.realpath(__file__)+'/displayShell/'+str(cmd), '|', 'grep', grep], stdout=subprocess.PIPE)
        return p

    def _readGPULoad():
        p = bashCommand("displayTemp.sh", "GPU load")
        return p.stdout.read()

    def _readTemp():
        p = bashCommand("displayTemp.sh", "Seonsor")
        return p.stdout.read()

    def _parseGPULoad():
        res = _readGPULoad()
        res_dic = res.strip().split("\n")
        return res_dic

    def _parseTemp():
        res = readTemp()
        resDic = res.strip().split("\n")
        final = [int(line.strip()[-7:-5]) for line in resDic if "Temperature" in line]
        return str(final).strip()



if __name__=="__main__":
    dataObj=dataHouse()
    print dataObj._parseGPULoad()
