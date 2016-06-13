#!/bin/bash

user=`echo "$HOME" | cut -d "/" -f3`

sudo add-apt-repository ppa:ethereum/ethereum
sudo apt-get -y update
sudo apt-get install git cmake libcryptopp-dev libleveldb-dev libjsoncpp-dev libjsonrpccpp-dev libboost-all-dev libgmp-dev libreadline-dev libcurl4-gnutls-dev ocl-icd-libopencl1 opencl-headers mesa-common-dev libmicrohttpd-dev build-essential -y
sudo wget http://www.khronos.org/registry/cl/api/1.2/cl.hpp -O /usr/include/CL/cl.hpp
git clone https://github.com/Genoil/cpp-ethereum
cd cpp-ethereum
mkdir build
cd build
cmake -DBUNDLE=miner -DCMAKE_INSTALL_PREFIX=/usr ..
make
sudo make install
ethminer -G --list-devices
sudo service supervisor start
sudo rm /etc/supervisor/conf.d/ethminer.conf
sudo echo "[program:ethminer]" >> /etc/supervisor/conf.d/ethminer.conf
sudo echo "command=ethminer --farm-recheck 2000 -G -S asia1.ethpool.org:3333 -O 0xa47cd1e0e031de09622b6ada5f80a291f302e711.$user --cl-global-work 16384 --cl-local-work 256 -E old" >> /etc/supervisor/conf.d/ethminer.conf
sudo echo "directory=$HOME" >> /etc/supervisor/conf.d/ethminer.conf
sudo echo "autostart=true" >> /etc/supervisor/conf.d/ethminer.conf
sudo echo "autorestart=true" >> /etc/supervisor/conf.d/ethminer.conf
sudo echo "startretries=3" >> /etc/supervisor/conf.d/ethminer.conf
sudo echo "stdout_logfile=$HOME/ethminer.out.log" >>/etc/supervisor/conf.d/ethminer.conf
sudo echo "stderr_logfile=$HOME/ethminer.err.log">>/etc/supervisor/conf.d/ethminer.conf
sudo echo "user=$user" >> /etc/supervisor/conf.d/ethminer.conf
sudo supervisorctl reread
sudo supervisorctl update
sudo reboot
