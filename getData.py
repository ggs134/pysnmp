import subprocess
import os
import psutil

class DataHouse:
    def __init__(self):
        self.temperature = self._parseTemp()
        self.gpuLoad = self._parseGPULoad()
        self.coreClock = self._parseCoreClock()
        self.memoryClock = self._parseMemoryClock()
        self.cpuPercent = self._getCPUPercent()
        self.virtualMemory = self._getVirtualMemory()
        self.swapMemory = self._getSwapMemory()
        self.networkUsage = self._getNetworkUsage()
        self.bootTime = self._getBootTime()
        self.ethminerProcess = self._getEthminerProcess()
        self.fanSpeeds = self._getAllFanSpeed()

    def update(self):
        self.temperature = self._parseTemp()
        self.gpuLoad = self._parseGPULoad()
        self.coreClock = self._parseCoreClock()
        self.memoryClock = self._parseMemoryClock()
        self.cpuPercent = self._getCPUPercent()
        self.virtualMemory = self._getVirtualMemory()
        self.swapMemory = self._getSwapMemory()
        self.networkUsage = self._getNetworkUsage()
        self.bootTime = self._getBootTime()
        self.ethminerProcess = self._getEthminerProcess()
        self.fanSpeeds = self._getAllFanSpeed()

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

    def _getCPUPercent(self):
        percentList = psutil.cpu_percent(interval=1, percpu=True)
        return percentList

    def _getVirtualMemory(self):
        vm = psutil.virtual_memory()
        return vm

    def _getSwapMemory(self):
        sm = psutil.swap_memory()
        return sm

    def _getNetworkUsage(self):
        nu = psutil.net_io_counters()
        return nu

    def _getBootTime(self):
        bt = psutil.boot_time()
        return bt

    def _getEthminerProcess(self):
        pid = os.popen("pidof ethminer").read().strip("\n")
        return psutil.Process(int(pid))

    def _getSingleFanSpeed(self, num):
        res = os.popen('env DISPLAY=:0.'+str(num)+' aticonfig --pplib-cmd "get fanspeed 0"').read()
        return res.strip().split()

    def _getAllFanSpeed(self):
        res = []
        for i in xrange(10):
            speed = self._getSingleFanSpeed(i)
            if speed == []:
                return res
            else:
                res.append(speed[-1].strip("%"))


if __name__=="__main__":
    dataObj = DataHouse()
    print dataObj._parseTemp()
    print dataObj._parseGPULoad()
    print dataObj._parseMemoryClock()
    print dataObj._getEthminerProcess()
    print dataObj.fanSpeeds
    # print dataObj._getCPUPercent()
