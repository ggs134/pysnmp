#!/usr/bin/env python

import os

user = os.environ["HOME"].split("/")[2]

def _findLineNumber(filename,text):
  with open(filename) as f:
    data = f.readlines()
  
  for i in data:
    print i

  for i in data:
    print i
    if text in i:
      return data.index(i)
    else:
      pass


def replaceCommandLine(filename):
  lineNum = _findLineNumber(filename, "command")
  with open(filename) as f:
    lines = f.readlines()
  lines[lineNum] = "command=ethminer --farm-recheck 2000 -G -S asia1.ethereum.miningpoolhub.com:20535 -O inditow."+ user +":rlagnlrud --cl-global-work 16384 --cl-local-work 256 -E old"
  with open(filename, "w") as f:
    f.writelines(lines)
  print "success!"


if __name__ == "__main__":
  replaceCommandLine("/etc/supervisor/conf.d/ethminer.conf")
