import subprocess
import os

class DataHouse:
    def __init__(self):
        pass

    def bashCommand(self, cmd, grep):
        p = subprocess.Popen(['/bin/bash', os.path.dirname(os.path.realpath(__file__))+'/displayShell/'+str(cmd), '|', 'grep', grep], stdout=subprocess.PIPE)
        return p

    def _readGPULoad(self,):
        p = self.bashCommand("displayClock.sh", "GPU")
        return p.stdout.read()

    def _readTemp(self):
        p = self.bashCommand("displayTemp.sh", "Seonsor")
        return p.stdout.read()

    def _readClock(self):
        p = self.bashCommand("displayClock.sh","Current")
        return p.stdout.read()

    def _parseGPULoad(self):
        res = self._readGPULoad()
        res_dic = res.strip().split("\n")
        return [line.strip()[-4:-1] for line in res_dic if "GPU load" in line]

    def _parseClock(self):
        res = self._readClock()
        res_dic = res.strip().split("\n")
        return [line.strip() for line in res_dic if "Current Clock" in line]

    def _parseMemoryClock(self):
        parsedClock = self._parseClock()
        return [line.split()[4] for line in parsedClock]

    def _parseCoreClock(self):
        parsedClock = self._parseClock()
        return [line.split()[3] for line in parsedClock]

    def _parseTemp(self):
        res = self._readTemp()
        resDic = res.strip().split("\n")
        final = [int(line.strip()[-7:-5]) for line in resDic if "Temperature" in line]
        return str(final).strip()



if __name__=="__main__":
    dataObj = DataHouse()
    print dataObj._parseClock()
    print dataObj._parseMemoryClock()
    print dataObj._parseCoreClock()
