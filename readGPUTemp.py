import subprocess
import os

class DataHouse:
    def __init__(self):
        pass

    def bashCommand(self, cmd, grep):
        p = subprocess.Popen(['/bin/bash', os.path.realpath(__file__)+'/displayShell/'+str(cmd), '|', 'grep', grep], stdout=subprocess.PIPE)
        return p

    def _readGPULoad(self,):
        p = self.bashCommand("displayClock.sh", "GPU load")
        return p.stdout.read()

    def _readTemp(self):
        p = self.bashCommand("displayTemp.sh", "Seonsor")
        return p.stdout.read()

    def _parseGPULoad(self):
        res = self._readGPULoad()
        res_dic = res.strip().split("\n")
        return res_dic

    def _parseTemp(self):
        res = self._readTemp()
        resDic = res.strip().split("\n")
        final = [int(line.strip()[-7:-5]) for line in resDic if "Temperature" in line]
        return str(final).strip()



if __name__=="__main__":
    dataObj = DataHouse()
    print dataObj._parseGPULoad()
