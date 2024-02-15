# Create a new user
import os,sys,base64

from lib.Core import *

username = input('Username: ')
password = input('Password: ')
if (os.path.exists(os.getcwd()+"/system/cfg/"+username+"_profile")):
    print(f'{Font.RED} User already exists.{Font.WHITE}')
else:
    # User Profile Array, use this format when you get user info
    dsarry = [username, password, os.getcwd()+"/usr/"+username]
    if not os.path.exists(os.getcwd()+"/usr/"+username):
        os.mkdir(os.getcwd()+"/usr/"+username)
    ToolBox.writeto(Encrypter.encB64str(dsarry), os.getcwd() +
                    "/system/cfg/"+username+"_profile")
    print('Done')
