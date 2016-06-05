import subprocess

def bashCommand(cmd):
    p = subprocess.Popen(['/bin/bash', cmd, '|', "grep", 'Sensor'], stdout=subprocess.PIPE)
    return p

def readTemp():
    p = bashCommand("./display.sh")
    return p.stdout.read()

def parseResult():
    res = readTemp()
    resDic = res.strip().split("\n")
    final = [float(line.strip()[-7:-2]) for line in resDic if "Temperature" in line]
    return final

if __name__=="__main__":
    print parseResult()
