# Waring!
# This file is important for MayDOS Community Edition
# DO NOT EDIT THIS FILE

from system.mdsc.Core import *
import system.mdsc.mash
import app.musicplay

# regist variables
username = ''
opsym = '#'
updir = ''

def __init__():
    try:
        tlda = "("+Font.BLUE+username+Font.WHITE+") "+updir+opsym+' '
        while 1:
            cmd = input(tlda)
            cmdck = cmd.lower()

            if(cmdck.split(' ')[0]=='echo'):
                print(cmdck.split('echo')[1])
            elif(cmdck == 'help'):
                print(
                    '''
                    使用手册：
                    echo        在屏幕上打印字符串
                    sof           执行任意可执行文件
                    sysver      显示系统版本
                    exit          退出MayDOS
                    del           删除文件
                    cat           读取文件并显示
                    mplay      播放音乐
                    clear         清屏
                    cuser        创建新用户
                    password 修改用户的密码
                    logout      登出MayDOS
                    直接输入将会执行bin和app目录下的文件
                    '''
                )
            elif(cmdck.startswith('sof')):
                tmpcmd = list(cmdck)
                del tmpcmd[0:4]
                tmpcmd = "".join(tmpcmd)
                if cmd.lower().endswith("?"):
                    print("用法：sof [-abspath 绝对路径] [-rltpath 相对路径]")
                elif tmpcmd.lower().startswith("-abspath"):
                    tmpcmd = list(tmpcmd)
                    del tmpcmd[0:9]
                    tmpcmd = "".join(tmpcmd)
                    os.system(f"start {tmpcmd}")
                else:
                    tmpcmd = list(tmpcmd)
                    del tmpcmd[0:9]
                    tmpcmd = "".join(tmpcmd)
                    os.system(f"start{os.getcwd()+tmpcmd}")
            elif(cmdck == 'sysver'):
                print('\n MayDOS Next[Community] Dev1.0\nDevCode: Firefly')
            elif(cmdck.startswith('rapp')):
                tmpcmd = cmdck.split('rapp')[1]
                tmpcmd1 =tmpcmd.split(' ')
                if cmd.lower().endswith("?"):
                    print("用法：rapp [所执行的应用名称]")
                else:
                    print(tmpcmd1)
                    if(os.path.exists(os.getcwd()+'/app/'+tmpcmd1[1]+".py")):
                        os.system(sys.executable+' ' +os.getcwd()+'/app/'+tmpcmd[1]+".py "+tmpcmd.split(tmpcmd.split(' ')[1]+' ')[1])
                    else:
                        print(f'rapp: {Font.RED} file not found.{Font.WHITE}')
            elif(cmdck == 'exit'):
                os.abort()
            elif(cmdck.split(' ')[0] =='mplay'):
                app.musicplay.play(cmdck.split(' ')[1])
            elif(cmdck == 'logout'):
                MDSCore.run()
            elif(cmdck == 'clear'):
                ToolBox.clear()
            elif(cmdck.startswith('del')):
                tmp = cmdck.split('del')
                yson = input('确定要删除吗？此操作不可逆！[y/n]')
                if(yson == 'y'):
                    os.system('del '+tmp[1])
                else:
                    pass
            elif(cmdck.startswith('cat')):
                tmp = cmdck.split('cat ')
                if(os.path.exists(tmp[1])):
                    print(ToolBox.readfile(tmp[1]))
                else:
                    print(f'cat: {Font.RED} no such file.{Font.WHITE}')
            else:
                #Try to find file in binary and app directory
                if(os.path.exists(os.getcwd()+"/bin/"+cmdck.split(' ')[0]+".py")):
                    os.system(sys.executable+" "+os.getcwd()+"/bin/"+cmdck.split(' ')[0]+".py "+cmdck.split(cmdck.split(' ')[0])[1])
                elif(os.path.exists(os.getcwd()+"/app/"+cmdck.split(' ')[0]+".py")):
                    os.system(sys.executable+" "+os.getcwd()+"/app/"+cmdck.split(' ')[0]+".py "+cmdck.split(cmdck.split(' ')[0])[1])
                else:
                    print(f'Mash: {Font.RED} no such file or directory.{Font.WHITE}')
    except Exception as e:
        #Ignoring risks and continuing to visit
        #
        print(e)
        print('\n')
        __init__()