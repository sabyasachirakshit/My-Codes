import sys
import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
import pygame
df=pd.read_excel("raildata.xlsx")
def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    for index, item in df.iterrows():
        textToSpeech(item['Train'], '3_music.mp3')
        textToSpeech(item['Name'], '4_music.mp3')
        textToSpeech(item['From'], '6_music.mp3')
        textToSpeech(item['Via'], '8_music.mp3')
        textToSpeech(item['To'], '10_music.mp3')
        textToSpeech(item['Platform'], '12_music.mp3')

        audios = [f"{i}_music.mp3" for i in range(1,13)]

        announcement = mergeAudios(audios)
        announcement.export(f"{item['Train']}_English.mp3", format="mp3")

def textToSpeech2(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
def generateAnnouncement2(filename):
    df = pd.read_excel(filename)
    for index, item in df.iterrows():
        textToSpeech2(item['From'], '2_hindi.mp3')
        textToSpeech2(item['Via'], '4_hindi.mp3')
        textToSpeech2(item['To'], '6_hindi.mp3')
        textToSpeech2(item['Train'], '8_hindi.mp3')
        textToSpeech2(item['Name'], '9_hindi.mp3')
        textToSpeech2(item['Platform'], '11_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,13)]

        announcement = mergeAudios(audios)
        announcement.export(f"{item['Train']}_Hindi.mp3", format="mp3")
if __name__ == "__main__":
    print("Now Generating Announcement...")
    generateAnnouncement("raildata.xlsx")
    generateAnnouncement2("raildata.xlsx")

from PyQt5.QtWidgets import QMainWindow,QApplication
from afridip import *
class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.announce)
        self.show()

    def announce(self):
        import time
        from datetime import datetime
        df = pd.read_excel("raildata.xlsx")
        print(df)

        def railstatus1(filename):
            df = pd.read_excel(filename)
            self.ui.screen.setText(f" Train No :  {df.Train[0]} \n Train Name : {df.Name[0]}\n From : {df.From[0]} \n Via : {df.Via[0]} \n To : {df.To[0]} \n Platform No : {df.Platform[0]} \n Time : {df.Train_Time[0]}")

        def railstatus2(filename):
            df = pd.read_excel(filename)
            self.ui.screen.setText(f" Train No : {df.Train[1]} \n Train Name : {df.Name[1]}\n From : {df.From[1]} \n Via : {df.Via[1]} \n To : {df.To[1]} \n Platform No : {df.Platform[1]} \n Time : {df.Train_Time[1]}")

        def railstatus3(filename):
            df = pd.read_excel(filename)
            self.ui.screen.setText(f" Train No :  {df.Train[2]} \n Train Name : {df.Name[2]}\n From : {df.From[2]} \n Via : {df.Via[2]} \n To : {df.To[2]} \n Platform No : {df.Platform[2]} \n Time : {df.Train_Time[2]}")

        def railstatus4(filename):
            df = pd.read_excel(filename)
            self.ui.screen.setText(f" Train No :  {df.Train[3]} \n Train Name : {df.Name[3]}\n From : {df.From[3]} \n Via : {df.Via[3]} \n To : {df.To[3]} \n Platform No : {df.Platform[3]} \n Time : {df.Train_Time[3]}")

        def railstatus5(filename):
            df = pd.read_excel(filename)
            self.ui.screen.setText(f" Train No :  {df.Train[4]} \n Train Name : {df.Name[4]}\n From : {df.From[4]} \n Via : {df.Via[4]} \n To : {df.To[4]} \n Platform No : {df.Platform[4]} \n Time : {df.Train_Time[4]}")

        def railstatus6(filename):
            df = pd.read_excel(filename)
            self.ui.screen.setText(f" Train No :  {df.Train[5]} \n Train Name : {df.Name[5]}\n From : {df.From[5]} \n Via : {df.Via[5]} \n To : {df.To[5]} \n Platform No : {df.Platform[5]} \n Time : {df.Train_Time[5]}")

        def railstatus7(filename):
            df = pd.read_excel(filename)
            self.ui.screen.setText(f" Train No :  {df.Train[6]} \n Train Name : {df.Name[6]}\n From : {df.From[6]} \n Via : {df.Via[6]} \n To : {df.To[6]} \n Platform No : {df.Platform[6]} \n Time : {df.Train_Time[6]}")

        def railstatus8(filename):
            df = pd.read_excel(filename)
            self.ui.screen.setText(f" Train No :  {df.Train[7]} \n Train Name : {df.Name[7]}\n From : {df.From[7]} \n Via : {df.Via[7]} \n To : {df.To[7]} \n Platform No : {df.Platform[7]} \n Time : {df.Train_Time[7]}")

        def railstatus9(filename):
            df = pd.read_excel(filename)
            self.ui.screen.setText(f" Train No :  {df.Train[8]} \n Train Name : {df.Name[8]}\n From : {df.From[8]} \n Via : {df.Via[8]} \n To : {df.To[8]} \n Platform No : {df.Platform[8]} \n Time : {df.Train_Time[8]}")

        def railstatus10(filename):
            df = pd.read_excel(filename)
            self.ui.screen.setText(f" Train No :  {df.Train[9]} \n Train Name : {df.Name[9]}\n From : {df.From[9]} \n Via : {df.Via[9]} \n To : {df.To[9]} \n Platform No : {df.Platform[9]} \n Time : {df.Train_Time[9]}")

        # def railstatus11(filename):
        #     df = pd.read_excel(filename)
        #     self.ui.screen.setText(f" Train No :  {df.Train[10]} \n Train Name : {df.Name[10]}\n From : {df.From[10]} \n Via : {df.Via[10]} \n To : {df.To[10]} \n Platform No : {df.Platform[10]} \n Time : {df.Train_Time[10]}")
        #
        # def railstatus12(filename):
        #     df = pd.read_excel(filename)
        #     self.ui.screen.setText(f" Train No :  {df.Train[11]} \n Train Name : {df.Name[11]}\n From : {df.From[11]} \n Via : {df.Via[11]} \n To : {df.To[11]} \n Platform No : {df.Platform[11]} \n Time : {df.Train_Time[11]}")
        #
        # def railstatus13(filename):
        #     df = pd.read_excel(filename)
        #     self.ui.screen.setText(f" Train No :  {df.Train[12]} \n Train Name : {df.Name[12]}\n From : {df.From[12]} \n Via : {df.Via[12]} \n To : {df.To[12]} \n Platform No : {df.Platform[12]} \n Time : {df.Train_Time[12]}")
        #
        # def railstatus14(filename):
        #     df = pd.read_excel(filename)
        #     self.ui.screen.setText(f" Train No :  {df.Train[13]} \n Train Name : {df.Name[13]}\n From : {df.From[13]} \n Via : {df.Via[13]} \n To : {df.To[13]} \n Platform No : {df.Platform[13]} \n Time : {df.Train_Time[13]}")
        #
        # def railstatus15(filename):
        #     df = pd.read_excel(filename)
        #     self.ui.screen.setText(f" Train No :  {df.Train[14]} \n Train Name : {df.Name[14]}\n From : {df.From[14]} \n Via : {df.Via[14]} \n To : {df.To[14]} \n Platform No : {df.Platform[14]} \n Time : {df.Train_Time[14]}")
        #
        # def railstatus16(filename):
        #     df = pd.read_excel(filename)
        #     self.ui.screen.setText(f" Train No :  {df.Train[15]} \n Train Name : {df.Name[15]}\n From : {df.From[15]} \n Via : {df.Via[15]} \n To : {df.To[15]} \n Platform No : {df.Platform[15]} \n Time : {df.Train_Time[15]}")
        #
        # def railstatus17(filename):
        #     df = pd.read_excel(filename)
        #     self.ui.screen.setText(f" Train No :  {df.Train[16]} \n Train Name : {df.Name[16]}\n From : {df.From[16]} \n Via : {df.Via[16]} \n To : {df.To[16]} \n Platform No : {df.Platform[16]} \n Time : {df.Train_Time[16]}")
        #
        # def railstatus18(filename):
        #     df = pd.read_excel(filename)
        #     self.ui.screen.setText(f" Train No :  {df.Train[17]} \n Train Name : {df.Name[17]}\n From : {df.From[17]} \n Via : {df.Via[17]} \n To : {df.To[17]} \n Platform No : {df.Platform[17]} \n Time : {df.Train_Time[17]}")
        #
        # def railstatus19(filename):
        #     df = pd.read_excel(filename)
        #     self.ui.screen.setText(f" Train No :  {df.Train[18]} \n Train Name : {df.Name[18]}\n From : {df.From[18]} \n Via : {df.Via[18]} \n To : {df.To[18]} \n Platform No : {df.Platform[18]} \n Time : {df.Train_Time[18]}")
        #
        # def railstatus20(filename):
        #     df = pd.read_excel(filename)
        #     self.ui.screen.setText(f" Train No :  {df.Train[19]} \n Train Name : {df.Name[19]}\n From : {df.From[19]} \n Via : {df.Via[19]} \n To : {df.To[19]} \n Platform No : {df.Platform[19]} \n Time : {df.Train_Time[19]}")

        def mergeAudios1(audios1):
            combined = AudioSegment.empty()
            for audio in audios1:
                combined += AudioSegment.from_mp3(audio)
            return combined

        def mixedmusic(number1):
            audios1 = [f"{number1}_Hindi.mp3", f"{number1}_English.mp3"]
            announcement = mergeAudios1(audios1)
            announcement.export(f"{number1}_mixedmusic.mp3", format="mp3")

        def music1(number):
            pygame.mixer.music.load(f"{number}_mixedmusic.mp3")
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play(3)


        Time0,Time1,Time2,Time3,Time4 = df.Time[0],df.Time[1],df.Time[2],df.Time[3],df.Time[4]
        Time5,Time6,Time7,Time8,Time9 = df.Time[5],df.Time[6],df.Time[7],df.Time[5],df.Time[9]
        # Time10,Time11,Time12,Time13,Time14 = df.Time[10],df.Time[11],df.Time[12],df.Time[13],df.Time[14]
        # Time15,Time16,Time17,Time18,Time19 = df.Time[15],df.Time[16],df.Time[17],df.Time[18],df.Time[19]

        Train0,Train1,Train2,Train3,Train4 = df.Train[0],df.Train[1],df.Train[2],df.Train[3],df.Train[4]
        Train5,Train6,Train7,Train8,Train9 = df.Train[5],df.Train[6],df.Train[7],df.Train[5],df.Train[9]
        # Train10,Train11,Train12,Train13,Train14 = df.Time[10],df.Time[11],df.Time[12],df.Time[13],df.Time[14]
        # Train15,Train16,Train17,Train18,Train19 = df.Time[15],df.Time[16],df.Time[17],df.Time[18],df.Time[19]


        while True:
            QApplication.processEvents()
            pygame.mixer.init()
            localtime1 = time.asctime(time.localtime(time.time()))
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.ui.clock.setText(f"{localtime1}")
            if current_time == str(Time0):
                railstatus1("raildata.xlsx")
                QApplication.processEvents()
                mixedmusic(Train0)
                music1(Train0)
            elif current_time == str(Time1):
                railstatus2("raildata.xlsx")
                QApplication.processEvents()
                mixedmusic(Train1)
                music1(Train1)
            elif current_time == str(Time2):
                railstatus3("raildata.xlsx")
                QApplication.processEvents()
                mixedmusic(Train2)
                music1(Train2)
            elif current_time == str(Time3):
                railstatus4("raildata.xlsx")
                QApplication.processEvents()
                mixedmusic(Train3)
                music1(Train3)
            elif current_time == str(Time4):
                railstatus5("raildata.xlsx")
                QApplication.processEvents()
                mixedmusic(Train4)
                music1(Train4)
            elif current_time == str(Time5):
                railstatus6("raildata.xlsx")
                QApplication.processEvents()
                mixedmusic(Train5)
                music1(Train5)
            elif current_time == str(Time6):
                railstatus7("raildata.xlsx")
                QApplication.processEvents()
                mixedmusic(Train6)
                music1(Train6)
            elif current_time == str(Time7):
                railstatus8("raildata.xlsx")
                QApplication.processEvents()
                mixedmusic(Train7)
                music1(Train7)
            elif current_time == str(Time8):
                railstatus9("raildata.xlsx")
                QApplication.processEvents()
                mixedmusic(Train8)
                music1(Train8)
            elif current_time == str(Time9):
                railstatus10("raildata.xlsx")
                QApplication.processEvents()
                mixedmusic(Train9)
                music1(Train9)
            # elif current_time == str(Time10):
            #     railstatus11("raildata.xlsx")
            #     # music1(Train10)
            # elif current_time == str(Time11):
            #     railstatus12("raildata.xlsx")
            #     # music1(Train11)
            # elif current_time == str(Time12):
            #     railstatus13("raildata.xlsx")
            #     # music1(Train12)
            # elif current_time == str(Time13):
            #     railstatus14("raildata.xlsx")
            #     # music1(Train13)
            # elif current_time == str(Time14):
            #     railstatus15("raildata.xlsx")
                # music1(Train14)
            # elif current_time == str(Time15):
            #     railstatus16("raildata.xlsx")
            #     music1(Train15)
            # elif current_time == str(Time16):
            #     railstatus17("raildata.xlsx")
            #     music1(Train16)
            # elif current_time == str(Time17):
            #     railstatus18("raildata.xlsx")
            #     music1(Train17)
            # elif current_time == str(Time18):
            #     railstatus19("raildata.xlsx")
            #     music1(Train18)
            # elif current_time == str(Time19):
            #     railstatus20("raildata.xlsx")
            #     music1(Train19)


if __name__ == "__main__":
    app =QApplication(sys.argv)
    w=MyForm()
    w.show()
    sys.exit(app.exec_())