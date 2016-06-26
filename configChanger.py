#-*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--miningpoolhub", help="change to miningpoolhub", action="store_true")
parser.add_argument("--ethpool", help="change to ethpool", action="store_true")
parser.add_argument("--environment", help="setting environment", action="store_true")
args = parser.parse_args()

#현재 사용자 이름을 홈디렉터리를 이용해서 추출
user = os.environ["HOME"].split("/")[2]


#파일의 해당 문자가 속해있는 줄을 찾아주는 함수
#filename의 파일을 읽어서 해당 text의 줄을 리턴해줌
def _findLineNumber(filename,text):
  with open(filename) as f:
    data = f.readlines()

  # for i in data:
    # print i

  for i in data:
    # print i
    if text in i:
      return data.index(i)
    else:
      pass


def _findSpecificLineAndReplace(filename, targetWord, replacingWord):
  linenum = _findLineNumber(filename, targetWord)
  #해당 명령이 섞인 줄이 있을 경우
  if linenum:
    with open(filename) as f:
      lines = f.readlines()
    lines[linenum] = replacingWord+"\n"
    with open(filename, "w") as f:
      f.writelines(lines)
  #없을경우 파일 끝에 append
  else:
    with open(filename, "a") as f:
      f.write(replacingWord+"\n")
  print "success!"

#ethminer를 마이닝풀허브로 이동시키는 함수
#filename을 읽어서 커맨드부분을 해당 커맨드로 변경
def replaceMiningPoolHub(filename):
  target = "command"
  substitute = "command=ethminer --farm-recheck 2000 -G -S asia1.ethereum.miningpoolhub.com:20535 -O inditow."+ user +":rlagnlrud --cl-global-work 16384 --cl-local-work 256 -E old"
  _findSpecificLineAndReplace(filename, target, substitute)

def replaceEthpool(filename):
  target = "command"
  substitute = "ethminer --farm-recheck 2000 -G -S asia1.ethpool.org:3333 -O 0xa47cd1e0e031de09622b6ada5f80a291f302e711.miner17 --cl-global-work 16384 --cl-local-work 256 -E old"
  _findSpecificLineAndReplace(filename, target, substitute)


#ethminer에 환경변수를 설정해주는 함수
#filename을 읽어서 environment변수들을 할당
def addEnvironment(filename):
  linenum = _findLineNumber(filename, "environment")
  #environment라인이 존재할 경우 해당 라인을 변경
  if linenum:
    with open(filename) as f:
      lines = f.readlines()
    lines[linenum] = "environment=GPU_FORCE_64BIT_PTR=0,GPU_MAX_HEAP_SIZE=100,GPU_USE_SYNC_OBJECTS=1,GPU_SINGLE_ALLOC_PERCENT=100\n"
    with open(filename, "w") as f:
      f.writelines(lines)
  #environment라인이 존재하지 않을 경우 파일 끝에 확장(append)
  else:
    with open(filename, "a") as f:
      f.write("environment=GPU_FORCE_64BIT_PTR=0,GPU_MAX_HEAP_SIZE=100,GPU_USE_SYNC_OBJECTS=1,GPU_SINGLE_ALLOC_PERCENT=100\n")

def commandOS(command):
  os.system(command)

if __name__ == "__main__":
  #목표가 되는 파일 
  targetFileName = "/etc/supervisor/conf.d/ethminer.conf"
  if args.miningpoolhub:
    # replaceCommandLine("/etc/supervisor/conf.d/ethminer.conf")
    replaceMiningPoolHub(targetFileName)
  elif args.ethpool:
    replaceEthpool(targetFileName)
  elif args.environment:
    addEnvironment(targetFileName)

  #수퍼바이저 세팅 다시 읽어서 업데이트
  commandOS("sudo supervsorctl reread")
  commandOS("sudo supervisorctl update")
