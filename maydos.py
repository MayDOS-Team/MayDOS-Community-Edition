# MayDOS Community Edition
# Attention! This version is independent of existing MayDOS versions
# And it is not related to the current MayDOS version

#Include neccessary modules

import os
import sys

#Check python version
#(minimum version Python 3.9.0)

if(sys.version_info.major < 3):
    print("Python version must be at least 3.9.0")
    os.abort(-1)
if( sys.version_info.minor < 9):
    print("Python version must be at least 3.9.0")
    os.abort(-1)

#Regist evironment variables

mdscversion = 'dev1.0'
sysroot = os.getcwd()
pypath = sys.executable

#Check important files

assert os.path.exists(sysroot+"/system"), "System directory does not exist, please reinstall system"
assert os.path.exists(sysroot+"/system/registTable.py"), "Missing regist file"
assert os.path.exists(sysroot+"/system/mdsc/Core.py"), "System core does not exist, please reinstall system"

try:
    import playsound
    import numpy
    import contextlib
    import wave
    import time
    import signal
except:
    os.system(sys.executable+' -m pip install playsound -i https://pypi.tuna.tsinghua.edu.cn/simple')
    os.system(sys.executable+' -m pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple')
    os.system(sys.executable+' -m pip install contextlib -i https://pypi.tuna.tsinghua.edu.cn/simple')
    os.system(sys.executable+' -m pip install wave -i https://pypi.tuna.tsinghua.edu.cn/simple')


#Include modules that do not require pip to download
#(single user only)

from system.mdsc.Core import *
import system.mdsc.Core as core

# Extra Settings
def ctrlc_handler(signal,frame):
    # Response Ctrl+c
    pass

#bind
signal.signal(signal.SIGINT,ctrlc_handler)

# Debug mode
dbgmd =True
if(dbgmd):
    import system.mdsc.mash as ms
    ms.__init__()
else:
    # Check whether installed
    if(os.path.exists(sysroot+"/system/.mdscinstalled")):
        core.MDSCore.run()
    else:
        #Run installer
        core.MDSCInstaller.run()