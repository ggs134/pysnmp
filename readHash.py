
filepath = "ethminer.err.log"

def hello():
    print "hi"

def getHash(path):
    with open(path) as f:
        lines = f.readlines()
        last = lines[-1]
        count = 0
        print last.split()[8][:-4]
        for i in last.split():
	    count+=1
            print count, i

if __name__=="__main__":
    getHash(filepath)
