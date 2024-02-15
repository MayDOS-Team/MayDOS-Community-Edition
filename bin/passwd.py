# Change user's password

import os,sys,base64

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

username = input('Username: ')
if not os.path.exists(os.getcwd()+"/system/cfg/"+username+"_profile"):
    print(f'{Font.RED} User not exists.{Font.WHITE}')
else:
    oldpw = input('Old password: ')
    pft = ToolBox.readfile(os.getcwd()+"/system/cfg/"+username+"_profile")
    pfarr = Encrypter.decB64str(''.join(pft))
    if (oldpw != pfarr[1]):
        print(f'{Font.RED} Password not match.{Font.WHITE}')
    else:
        newpw = input('New password: ')
        dsarry = [username, newpw, os.getcwd()+"/usr/"+username]
        ToolBox.writeto(Encrypter.encB64str(dsarry),
                        os.getcwd() + "/system/cfg/"+username+"_profile")
