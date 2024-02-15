# Waring!
# This file is important for MayDOS Community Edition
# DO NOT EDIT THIS FILE though you are the professional engineer
# If you find bugs, please send pr at github

#Import modules

import base64
import os
import sys
import time

#OShell installer
class MDSCInstaller:
    '''MDSC installer class'''
    def run():
        '''Run installer'''
        print('Please wait')
        time.sleep(2)

        # Screen 1
        # Lead in
        ToolBox.clear()
        print('Welcome to MayDOS Community Edition dev1.0 installer')
        print('[Development version does not represent final quality]\n\n\n')
        print('Press any key to continue...')
        ToolBox.waitkey()

        # Screen 2
        # Select Language
        ToolBox.clear()
        print('Step 1: Select Language\n\n')

        # Development Version only supports Chinese

        # print("1. Chinese[zh-cn]\n2.English[en-US]")
        # langset = input("Enter number you select:")
        print('Sorry. Development version only supports Chinese\n\nPress any key to continue...')
        ToolBox.waitkey()

        # Screen 3
        # Set user
        ToolBox.clear()
        print('Step 2: Set user')
        print(Style.ITALIC+Font.RED + '[You can add more user when you finished installation]'+Style.END+Font.WHITE)
        print('\n\n')
        while 1:
            username = input("User name: ")
            if(' ' in username):
                print('User name cant contain spaces')
            else:
                break
        password = input("Password: ")

        # Screen 4
        # Install
        ToolBox.clear()
        print('Step 3: Install')
        print('\n\n')
        print('user:'+username)
        print('password:'+password)
        print('After confirming the correctness, press Enter to proceed with installation')
        print('If not correct, please exit the installation program and try again')
        ToolBox.waitkey()

        # Install
        # Write install file
        print('\n\n\n Please wait for the installation')
        ToolBox.writeto("",os.getcwd()+"/system/.mdscinstalled")
        # Save User Profile
        dsarry = [username,password,os.getcwd()+"/usr/"+username] # User Profile Array, use this format when you get user info
        if not os.path.exists(os.getcwd()+"/usr/"+username):
            os.mkdir(os.getcwd()+"/usr/"+username)
        ToolBox.writeto(Encrypter.encB64str(dsarry),os.getcwd()+"/system/cfg/"+username+"_profile")
        print('Done')
        print('Press any key to continue...')
        ToolBox.waitkey()
        MDSCore.run()


class MDSCore():
    def run():
        import system.mdsc.mash # Console Mash
        ToolBox.clear()
        # Login
        print('登录到 MayDOS\n\n')
        while 1:
            print('\n')
            unm = input('用户名：')
            upw = input('密码：')
            
            if not os.path.exists(os.getcwd()+"/system/cfg/"+unm+"_profile"):
                print(Font.RED+"用户不存在！"+Font.WHITE)
            else:
                pft = ToolBox.readfile(os.getcwd()+"/system/cfg/"+unm+"_profile")
                pfarr = Encrypter.decB64str(''.join(pft))
                if(unm != pfarr[0]):
                    print(Font.RED+"用户不存在！"+Font.WHITE)
                elif(upw !=pfarr[1]):
                    print(Font.RED+"密码错误！"+Font.WHITE)
                else:
                    print('\n欢迎！\n')
                    break
        system.mdsc.mash.username = unm
        system.mdsc.mash.updir = ''
        system.mdsc.mash.__init__()

#Tool Box class
class ToolBox():
    '''Toolbox Class'''
    def clear():
        print('\033c')
    
    def waitkey():
        os.system('pause')

    def writeto(text,path):
        os.system('echo '+text+">"+path)
    def addto(text,path):
        os.system('echo '+text+">>"+path)
    def readfile(path):
        with open(path,'r',encoding='utf-8') as f:
            return f.read()

#Console Style
class Style:
    END = '\33[0m'
    BOLD = '\33[1m'
    ITALIC = '\33[3m'
    URL = '\33[4m'
    BLINK = '\33[5m'
    BLINK2 = '\33[6m'
    SELECTED = '\33[7m'


class Font:
    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE = '\33[36m'
    WHITE = '\33[37m'


class Background:
    BLACK = '\33[40m'
    RED = '\33[41m'
    GREEN = '\33[42m'
    YELLOW = '\33[43m'
    BLUE = '\33[44m'
    VIOLET = '\33[45m'
    BEIGE = '\33[46m'
    WHITE = '\33[47m'

class Encrypter:
    def encB64str(strarry:list):
        '''Get Base64 Str from a arry'''
        txt = ''
        for i in strarry:
            p = str(base64.b64encode(bytes(i,encoding="utf-8")),encoding='utf-8')
            txt += p
            txt +='.'
        return txt
    
    def decB64str(strf:str):
        '''Decode Base64 Str from a string'''
        resar = []
        strt = strf.split('.')
        for i in strt:
            res = str(base64.b64decode(i),encoding='utf-8')
            resar.append(res)
        return resar

class Progressbar:
    def __init__(self, message: str="正在更新中", mode: int=0, sleep_time: float=0.02):
        self.mode: int = mode
        self.message: str = message
        self.sleep_time: float = sleep_time

    def start(self):
        if self.mode == 0:
            for i in range(1, 101):
                print('\r', end="")
                print(str(self.message), f"{i}%", "▌" * (i // 2), end='')
                sys.stdout.flush()
                time.sleep(self.sleep_time) #刷新输出区，否则以上进度条不会立马显示
        if self.mode == 1:
            for i in range(1, 101):
                print('\r', end="")
                print(str(self.message), f"{i}%", "▋" * (i // 2), end='')
                sys.stdout.flush()
                time.sleep(self.sleep_time) #刷新输出区，否则以上进度条不会立马显示