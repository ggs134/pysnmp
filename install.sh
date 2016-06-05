#!bin/bash

sudo apt-get -y update                               #업데이트
sudo apt-get -y install python-pip 	         #pip 설치
sudo pip install -y --upgrade pip                 #pip업그레이드
sudo apt-get -y install python-dev              #파이썬 디벨로퍼 버전 설치
sudo pip install pysnmp                         #pysnmp설치
sudo apt-get install -y libsmi2ldbl
sudo apt-get install -y python-pysnmp4
sudo apt-get install -y smilint
sudo apt-get install -y snmp snmp-mibs-downloader   #MIB데이터 다운로드
sudo apt-get install -y supervisor

##supervisor세팅
mkdir -p '$home/log'
#monitor.conf파일 설치

#agent.conf파일 세팅
