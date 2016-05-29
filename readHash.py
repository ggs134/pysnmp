
filepath = "/home/miner11/ethminer.err.log"

def hello():
    print "hi"

def getHash(path)
    with open(path) as f:
        lines = f.readlines()
        last = lines[-1]

        if last.startswith("miner") == False:
            getHash(path)

        for i in last:
            print i

if __name__=="__main__":
    getHash(filepath)
