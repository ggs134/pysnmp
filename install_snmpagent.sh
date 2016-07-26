#!/bin/bash

apt-get -y update                               #업데이트
apt-get -y install python-pip 	         #pip 설치
pip install -y --upgrade pip                 #pip업그레이드
apt-get -y install python-dev              #파이썬 디벨로퍼 버전 설치
pip install pysnmp                         #pysnmp설치
apt-get install -y libsmi2ldbl
apt-get install -y python-pysnmp4
apt-get install -y smilint
apt-get install -y snmp snmp-mibs-downloader   #MIB데이터 다운로드
apt-get install -y supervisor screen xinit
dpkg-reconfigure x11-common
pip install psutil

build-pysnmp-mib -o $HOME/pysnmp/MY-MIB.py $HOME/pysnmp/MY-MIB

##supervisor세팅
mkdir -p $HOME/log

#monitor.conf파일 세팅
#agent.conf파일 세팅
rm /etc/supervisor/conf.d/monitor.conf
rm /etc/supervisor/conf.d/agent.conf
python "monitor_and_agent_install.py"

#supervisor에서 읽어들임
supervisorctl reread
supervisorctl update
