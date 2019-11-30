# CanSat-software README.md

# Needed Parts
・Raspberry Pi 3 B
・BME280 module
・mpu6050 module
・neo6-m GPS module

# Raspberry Pi setup commands
- OS-update
    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get dist-upgrede
    $ sudo rpi-update
    $ sudo reboot

- Install needed packeges
    $ sudo apt-get install git gcc make openssl python3-dev
    $ sudo apt-get install libssl-dev libbz2-dev libreadline-dev libsqlite3-dev
    $ sudo apt-get install tk-dev python-tk libfreetype6-dev 
    $ sudo apt-get install pkg-config libjpeg8-dev libpng12-dev
    $ sudo apt-get install python3-numpy python3-scipy python3-matplotlib python3-h5py 
    $ sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev libc6-dev

- Install Numpy,imaging,pandas,matplotlib
    $ sudo apt-get install python3-numpy
    $ sudo apt-get install python3-imaging
    $ sudo apt-get install python3-pandas
    $ sudo apt-get install python3-matplotlib

- pip update
    $ sudo pip3 install -U pip
    $ sudo pip3 install -U setuptools

- Install Tensorflow
    $ sudo apt-get install libhdf5-dev
    $ sudo apt install libatlas-base-dev
    $ sudo pip3 --default-timeout=1000 install tensorflow==1.13.1
    ※Download .whl File from piwheels (https://www.piwheels.org/simple/tensorflow)
    move the file to home/pi directory then....
    $ sudo pip3 install ./tensorflow-1.14.0-cp35-none-linux_armv7l.whl

- Install Keras
    $ sudo pip3 install keras==2.2.2

- Install OpenCV
    $ sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-100
    $ sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
    $ sudo apt-get install libatlas-base-dev
    $ sudo apt-get install libjasper-dev
    $ curl -SL https://github.com/mt08xx/files/raw/master/opencv-rpi/libopencv3_3.4.6-20190415.1_armhf.deb -o libopencv3_3.4.6-20190415.1_armhf.deb
    $ sudo apt install -y ./libopencv3_3.4.6-20190415.1_armhf.deb

- Install camera module
    $ sudo apt-get install python3-picamera

- Install I2C module
    $ sudo apt-get install libi2c-dev
    $ sudo apt-get install i2c-tools
    $ sudo apt-get install python3-smbus