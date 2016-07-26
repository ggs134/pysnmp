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
