import numpy as np
import sounddevice as sd
import time


class RltPitchCalc():
    ''' Real Time 8-bit Player Pitch Table

    A table of pitches and calculate

    '''
    # 基准音，可以直接调用
    C4 = 262
    D4 = 294
    E4 = 330
    F4 = 349
    G4 = 392
    A4 = 440
    B4 = 494

    def __init__(self) -> None:
        self.C4 = 262
        self.D4 = 294
        self.E4 = 330
        self.F4 = 349
        self.G4 = 392
        self.A4 = 440
        self.B4 = 494
    # 计算方法
    # 全音是2倍关系
    # 半音是全音的1.06倍

    def calc(self, snd: str) -> int:
        '''Calculator

        Calculates the high of the pitch

        Args:
            snd (str): The note to calculate, such as C4, D4

        Returns:
            int: The frequency of the pitch
        '''
        # 判断是否符合格式
        ## 格式：C4,C4b##
        if len(snd) > 3 or len(snd) < 2:
            raise TypeError(snd + 'not a true note type.')
        
        note_dict = {
            "C": self.C4,
            "D": self.D4,
            "E": self.E4,
            "F": self.F4,
            "G": self.G4,
            "A": self.A4,
            "B": self.B4
        }
        
        note = snd[0]
        octave = int(snd[1])
        modifier = snd[2] if len(snd) == 3 else None
        
        if note not in note_dict:
            raise ValueError("Invalid note: " + snd)
        
        base_freq = note_dict[note]
        
        if octave < 4:
            freq = base_freq / (2 * (4 - octave))
        elif octave == 4:
            freq = base_freq
        else:
            freq = base_freq * (2 * (octave - 4))
        
        if modifier == "#":
            freq *= 1.06
        elif modifier == "b":
            freq /= 1.06
        
        return freq

class RltPlayer():
    ''' Real Time 8-bit Player
    '''

    def __init__(self, fs: int):
        ''' Real Time 8-bit Player Init


            Args:
                    fs (int): The sampling rate of the song next
        '''
        self.fs = fs

    def sine(self, f: int, length: int):
        ''' Real Time 8-bit Player Sine Wave Player


            Args:
                    f (int): The frequency of the wave
                    length (int): The length of the playback time
        '''
        # f = 263 # 音频频率Hz
        # length = 2 #时长s
        myarray = np.arange(self.fs * length)  # 用numpy生成2000Hz的正弦波
        myarray = np.sin(2 * np.pi * f / self.fs * myarray)
        # print('显示数组内容:',myarray)
        sd.play(myarray, self.fs)  # 播放
        time.sleep(length)

    def square(self,f:int,length:int):
        ''' Real Time 8-bit Player Square Wave Player


            Args:
                    f (int): The frequency of the wave
                    length (int): The length of the playback time
        '''
        t = np.arange(0,length,1/self.fs)
        sqwave = np.sign(np.sin(2*np.pi*f*t))
        sd.play(sqwave, self.fs)  # 播放
        time.sleep(length)

    def sawtooth(self,f:int,length:int):
            ''' Real Time 8-bit Player Sawtooth Wave Player


                Args:
                        f (int): The frequency of the wave
                        length (int): The length of the playback time
            '''
            t = np.arange(0,length,1/self.fs)
            sawave = np.mod(2*np.pi*f*t,2*np.pi)
            sawave = sawave / np.pi
            sd.play(sawave, self.fs)  # 播放
            time.sleep(length)

    def noise(self,length:int):
            ''' Real Time 8-bit Player White Noise Player


                Args:
                        length (int): The length of the playback time
            '''
            t = np.arange(0,length,1/self.fs)
            wn = np.random.normal(0,1,len(t))
            sd.play(wn, self.fs)  # 播放
            time.sleep(length)


class RltFilePlayer():
    '''Real Time 8-bit File Player

    A easy tool to read "Special Music File"(*.music in a certain format), and turn it into playable 8-bit music
    '''

    def __init__(self):
        self.rawMusic = {}

    def readFile(self,filepath:str):
        '''FileReader
        
        Read *.music File and analysis it to playable music

        Args:
                filepath (str): The file to read
        '''

        #从文件读取
        fileHandler = open(filepath,"r")
        while 1:
            #循环读取并存储在内存中
            tline = fileHandler.readline()
            if(itb==0):
                if(tline.split(' ')[0]=="SampRate"):
                    self.rltplayer = RltPlayer(int(tline.split(' ')[1]))
                    self.samprate = int(tline.split(' ')[1])
                if(tline.split(' ')[0]=="TraceNum"):
                    self.traceNum = int(tline.split(' ')[1])
                if(tline.split(' ')[0]=="Trace" and tline.split(' ')[1]=="Begin"):
                    tarln = int(tline.split(' ')[2])
                    print(tarln)
                    itb = 1
            else:
                if(tline.split(' ')[0]=="Trace" and tline.split(' ')[1]=="End"):
                    itb=0
                else:
                    self.rawMusic[str(tarln)] +=tline
            if not tline:
                break
        fileHandler.close()

    def getDetails(self):
        '''Details Geter

        Get the details of the file which was loaded
        '''
        print("Sampling Rate: "+str(self.samprate))
        print("Total Trace: "+str(self.traceNum))
        print("Raw Trace: "+str(self.rawMusic))