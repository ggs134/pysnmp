sudo apt-get update
sudo apt-get install -y unzip git python-twisted software-properties-common supervisor screen
unzip ADL_SDK9.zip
tar -vxf AMD-APP-SDKInstaller-v3.0.130.136-GA-linux64.tar.bz2
sudo ./AMD-APP-SDK-v3.0.130.136-GA-linux64.sh
sudo ln -s /opt/AMDAPPSDK-3.0  /opt/AMDAPP
sudo ln -s /opt/AMDAPP/include/CL /usr/includeun
sudo ln -s /opt/AMDAPP/lib/x86_64/* /usr/lib/
sudo ldconfig
sudo reboot
