import sys
import os
import pandas as pd
# from pydub import AudioSegment
# from gtts import gTTS
# import pygame
df=pd.read_excel("raildata.xlsx")
# def textToSpeech(text, filename):
#     mytext = str(text)
#     language = 'en'
#     myobj = gTTS(text=mytext, lang=language, slow=False)
#     myobj.save(filename)
#
# def mergeAudios(audios):
#     combined = AudioSegment.empty()
#     for audio in audios:
#         combined += AudioSegment.from_mp3(audio)
#     return combined
#
# def generateAnnouncement(filename):
#     df = pd.read_excel(filename)
#     for index, item in df.iterrows():
#         textToSpeech(item['Train'], '3_music.mp3')
#         textToSpeech(item['Name'], '4_music.mp3')
#         textToSpeech(item['From'], '6_music.mp3')
#         textToSpeech(item['Via'], '8_music.mp3')
#         textToSpeech(item['To'], '10_music.mp3')
#         textToSpeech(item['Platform'], '12_music.mp3')
#
#         audios = [f"{i}_music.mp3" for i in range(1,13)]
#
#         announcement = mergeAudios(audios)
#         announcement.export(f"{item['Train']}_English.mp3", format="mp3")
#
# def textToSpeech2(text, filename):
#     mytext = str(text)
#     language = 'hi'
#     myobj = gTTS(text=mytext, lang=language, slow=False)
#     myobj.save(filename)
# def generateAnnouncement2(filename):
#     df = pd.read_excel(filename)
#     for index, item in df.iterrows():
#         textToSpeech2(item['From'], '2_hindi.mp3')
#         textToSpeech2(item['Via'], '4_hindi.mp3')
#         textToSpeech2(item['To'], '6_hindi.mp3')
#         textToSpeech2(item['Train'], '8_hindi.mp3')
#         textToSpeech2(item['Name'], '9_hindi.mp3')
#         textToSpeech2(item['Platform'], '11_hindi.mp3')
#
#         audios = [f"{i}_hindi.mp3" for i in range(1,13)]
#
#         announcement = mergeAudios(audios)
#         announcement.export(f"{item['Train']}_Hindi.mp3", format="mp3")
# if __name__ == "__main__":
#     print("Now Generating Announcement...")
#     generateAnnouncement("raildata.xlsx")
#     generateAnnouncement2("raildata.xlsx")

from PyQt5.QtWidgets import QMainWindow,QApplication
from afridip1 import *
from guirail2 import MyForm2
from guirail3 import MyForm3
class MyForm1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.status.clicked.connect(self.statusdisplay)
        self.ui.turnon.clicked.connect(self.maindisplay)
        self.ui.location.clicked.connect(self.locationdisplay)
        self.show()

    def locationdisplay(self):
        self.w = MyForm3()
        self.w.show()
    def statusdisplay(self):
        self.w = MyForm2()
        self.w.show()
    def maindisplay(self):
        import time
        from datetime import datetime
        df = pd.read_excel("raildata.xlsx")
        while True:
            QApplication.processEvents()
            localtime1 = time.asctime(time.localtime(time.time()))
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.ui.dc.setText(f"WELCOME TO INDIAN RAILWAYS      {localtime1}      WELCOME TO INDIAN RAILWAYS")
            self.ui.cn.setText(f" ")
            self.ui.tr1.setText(f" ")
            self.ui.tr2.setText(f" ")
            self.ui.tr3.setText(f" ")
            self.ui.tr4.setText(f" ")
            self.ui.tr5.setText(f" ")
            self.ui.tr6.setText(f" ")
            self.ui.tr7.setText(f" ")
            self.ui.tr8.setText(f" ")
            self.ui.tr9.setText(f" ")
            self.ui.tr10.setText(f" ")

            self.ui.tn.setText(f"TRAIN NO")
            if current_time <= str(df.At[0]) :
                self.ui.tn0.setText(f"{df.Train[0]}")
            elif current_time <= str(df.At[10]):
                self.ui.tn0.setText(f"{df.Train[10]}")
            elif current_time <= str(df.At[20]):
                self.ui.tn0.setText(f"{df.Train[20]}")
            elif current_time <= str(df.At[30]):
                self.ui.tn0.setText(f"{df.Train[30]}")
            elif current_time <= str(df.At[40]):
                self.ui.tn0.setText(f"{df.Train[40]}")
            else:
                self.ui.tn0.setText(f"0   0   0   0   0 ")
            if current_time <= str(df.At[1]):
                self.ui.tn1.setText(f"{df.Train[1]}")
            elif current_time <= str(df.At[11]):
                self.ui.tn1.setText(f"{df.Train[11]}")
            elif current_time <= str(df.At[21]):
                self.ui.tn1.setText(f"{df.Train[21]}")
            elif current_time <= str(df.At[31]):
                self.ui.tn1.setText(f"{df.Train[31]}")
            elif current_time <= str(df.At[41]):
                self.ui.tn1.setText(f"{df.Train[41]}")
            else:
                self.ui.tn1.setText(f"0   0   0   0   0 ")
            if current_time <= str(df.At[2]):
                self.ui.tn2.setText(f"{df.Train[2]}")
            elif current_time <= str(df.At[12]):
                self.ui.tn2.setText(f"{df.Train[12]}")
            elif current_time <= str(df.At[22]):
                self.ui.tn2.setText(f"{df.Train[22]}")
            elif current_time <= str(df.At[32]):
                self.ui.tn2.setText(f"{df.Train[32]}")
            elif current_time <= str(df.At[42]):
                self.ui.tn2.setText(f"{df.Train[42]}")
            else:
                self.ui.tn2.setText(f"0   0   0   0   0 ")
            if current_time <= str(df.At[3]):
                self.ui.tn3.setText(f"{df.Train[3]}")
            elif current_time <= str(df.At[13]):
                self.ui.tn3.setText(f"{df.Train[13]}")
            elif current_time <= str(df.At[23]):
                self.ui.tn3.setText(f"{df.Train[23]}")
            elif current_time <= str(df.At[33]):
                self.ui.tn3.setText(f"{df.Train[33]}")
            elif current_time <= str(df.At[43]):
                self.ui.tn3.setText(f"{df.Train[43]}")
            else:
                self.ui.tn3.setText(f"0   0   0   0   0 ")
            if current_time <= str(df.At[4]):
                self.ui.tn4.setText(f"{df.Train[4]}")
            elif current_time <= str(df.At[14]):
                self.ui.tn4.setText(f"{df.Train[14]}")
            elif current_time <= str(df.At[24]):
                self.ui.tn4.setText(f"{df.Train[24]}")
            elif current_time <= str(df.At[34]):
                self.ui.tn4.setText(f"{df.Train[34]}")
            elif current_time <= str(df.At[44]):
                self.ui.tn4.setText(f"{df.Train[44]}")
            else:
                self.ui.tn4.setText(f"{df.Train[44]}")
            if current_time <= str(df.At[5]):
                self.ui.tn5.setText(f"{df.Train[5]}")
            elif current_time <= str(df.At[15]):
                self.ui.tn5.setText(f"{df.Train[15]}")
            elif current_time <= str(df.At[25]):
                self.ui.tn5.setText(f"{df.Train[25]}")
            elif current_time <= str(df.At[35]):
                self.ui.tn5.setText(f"{df.Train[35]}")
            elif current_time <= str(df.At[45]):
                self.ui.tn5.setText(f"{df.Train[45]}")
            else:
                self.ui.tn5.setText(f"{df.Train[45]}")
            if current_time <= str(df.At[6]):
                self.ui.tn6.setText(f"{df.Train[6]}")
            elif current_time <= str(df.At[16]):
                self.ui.tn6.setText(f"{df.Train[16]}")
            elif current_time <= str(df.At[26]):
                self.ui.tn6.setText(f"{df.Train[26]}")
            elif current_time <= str(df.At[36]):
                self.ui.tn6.setText(f"{df.Train[36]}")
            elif current_time <= str(df.At[46]):
                self.ui.tn6.setText(f"{df.Train[46]}")
            else:
                self.ui.tn6.setText(f"{df.Train[46]}")
            if current_time <= str(df.At[7]):
                self.ui.tn7.setText(f"{df.Train[7]}")
            elif current_time <= str(df.At[17]):
                self.ui.tn7.setText(f"{df.Train[17]}")
            elif current_time <= str(df.At[27]):
                self.ui.tn7.setText(f"{df.Train[27]}")
            elif current_time <= str(df.At[37]):
                self.ui.tn7.setText(f"{df.Train[37]}")
            elif current_time <= str(df.At[47]):
                self.ui.tn7.setText(f"{df.Train[47]}")
            else:
                self.ui.tn7.setText(f"{df.Train[47]}")
            if current_time <= str(df.At[8]):
                self.ui.tn8.setText(f"{df.Train[8]}")
            elif current_time <= str(df.At[18]):
                self.ui.tn8.setText(f"{df.Train[18]}")
            elif current_time <= str(df.At[28]):
                self.ui.tn8.setText(f"{df.Train[28]}")
            elif current_time <= str(df.At[38]):
                self.ui.tn8.setText(f"{df.Train[38]}")
            elif current_time <= str(df.At[48]):
                self.ui.tn8.setText(f"{df.Train[48]}")
            else:
                self.ui.tn8.setText(f"{df.Train[48]}")
            if current_time <= str(df.At[9]):
                self.ui.tn9.setText(f"{df.Train[9]}")
            elif current_time <= str(df.At[19]):
                self.ui.tn9.setText(f"{df.Train[19]}")
            elif current_time <= str(df.At[29]):
                self.ui.tn9.setText(f"{df.Train[29]}")
            elif current_time <= str(df.At[39]):
                self.ui.tn9.setText(f"{df.Train[39]}")
            elif current_time <= str(df.At[49]):
                self.ui.tn9.setText(f"{df.Train[49]}")
            else:
                self.ui.tn9.setText(f"{df.Train[49]}")


            self.ui.tname.setText(f"TRAIN NAME")
            if current_time <= str(df.At[0]):
                self.ui.tname0.setText(f"{df.Name[0]}")
            elif current_time <= str(df.At[10]):
                self.ui.tname0.setText(f"{df.Name[10]}")
            elif current_time <= str(df.At[20]):
                self.ui.tname0.setText(f"{df.Name[20]}")
            elif current_time <= str(df.At[30]):
                self.ui.tname0.setText(f"{df.Name[30]}")
            elif current_time <= str(df.At[40]):
                self.ui.tname0.setText(f"{df.Name[40]}")
            else:
                self.ui.tname0.setText(f"Welcome To Indian Railways ")
            if current_time <= str(df.At[1]):
                self.ui.tname1.setText(f"{df.Name[1]}")
            elif current_time <= str(df.At[11]):
                self.ui.tname1.setText(f"{df.Name[11]}")
            elif current_time <= str(df.At[21]):
                self.ui.tname1.setText(f"{df.Name[21]}")
            elif current_time <= str(df.At[31]):
                self.ui.tname1.setText(f"{df.Name[31]}")
            elif current_time <= str(df.At[41]):
                self.ui.tname1.setText(f"{df.Name[41]}")
            else:
                self.ui.tname1.setText(f"Welcome To Indian Railways ")
            if current_time <= str(df.At[2]):
                self.ui.tname2.setText(f"{df.Name[2]}")
            elif current_time <= str(df.At[12]):
                self.ui.tname2.setText(f"{df.Name[12]}")
            elif current_time <= str(df.At[22]):
                self.ui.tname2.setText(f"{df.Name[22]}")
            elif current_time <= str(df.At[32]):
                self.ui.tname2.setText(f"{df.Name[32]}")
            elif current_time <= str(df.At[42]):
                self.ui.tname2.setText(f"{df.Name[42]}")
            else:
                self.ui.tname2.setText(f"Welcome To Indian Railways ")
            if current_time <= str(df.At[3]):
                self.ui.tname3.setText(f"{df.Name[3]}")
            elif current_time <= str(df.At[13]):
                self.ui.tname3.setText(f"{df.Name[13]}")
            elif current_time <= str(df.At[23]):
                self.ui.tname3.setText(f"{df.Name[23]}")
            elif current_time <= str(df.At[33]):
                self.ui.tname3.setText(f"{df.Name[33]}")
            elif current_time <= str(df.At[43]):
                self.ui.tname3.setText(f"{df.Name[43]}")
            else:
                self.ui.tname3.setText(f"Welcome To Indian Railways ")
            if current_time <= str(df.At[4]):
                self.ui.tname4.setText(f"{df.Name[4]}")
            elif current_time <= str(df.At[14]):
                self.ui.tname4.setText(f"{df.Name[14]}")
            elif current_time <= str(df.At[24]):
                self.ui.tname4.setText(f"{df.Name[24]}")
            elif current_time <= str(df.At[34]):
                self.ui.tname4.setText(f"{df.Name[34]}")
            elif current_time <= str(df.At[44]):
                self.ui.tname4.setText(f"{df.Name[44]}")
            else:
                self.ui.tname4.setText(f"{df.Name[44]}")
            if current_time <= str(df.At[5]):
                self.ui.tname5.setText(f"{df.Name[5]}")
            elif current_time <= str(df.At[15]):
                self.ui.tname5.setText(f"{df.Name[15]}")
            elif current_time <= str(df.At[25]):
                self.ui.tname5.setText(f"{df.Name[25]}")
            elif current_time <= str(df.At[35]):
                self.ui.tname5.setText(f"{df.Name[35]}")
            elif current_time <= str(df.At[45]):
                self.ui.tname5.setText(f"{df.Name[45]}")
            else:
                self.ui.tname5.setText(f"{df.Name[45]}")
            if current_time <= str(df.At[6]):
                self.ui.tname6.setText(f"{df.Name[6]}")
            elif current_time <= str(df.At[16]):
                self.ui.tname6.setText(f"{df.Name[16]}")
            elif current_time <= str(df.At[26]):
                self.ui.tname6.setText(f"{df.Name[26]}")
            elif current_time <= str(df.At[36]):
                self.ui.tname6.setText(f"{df.Name[36]}")
            elif current_time <= str(df.At[46]):
                self.ui.tname6.setText(f"{df.Name[46]}")
            else:
                self.ui.tname6.setText(f"{df.Name[46]}")
            if current_time <= str(df.At[7]):
                self.ui.tname7.setText(f"{df.Name[7]}")
            elif current_time <= str(df.At[17]):
                self.ui.tname7.setText(f"{df.Name[17]}")
            elif current_time <= str(df.At[27]):
                self.ui.tname7.setText(f"{df.Name[27]}")
            elif current_time <= str(df.At[37]):
                self.ui.tname7.setText(f"{df.Name[37]}")
            elif current_time <= str(df.At[47]):
                self.ui.tname7.setText(f"{df.Name[47]}")
            else:
                self.ui.tname7.setText(f"{df.Name[47]}")
            if current_time <= str(df.At[8]):
                self.ui.tname8.setText(f"{df.Name[8]}")
            elif current_time <= str(df.At[18]):
                self.ui.tname8.setText(f"{df.Name[18]}")
            elif current_time <= str(df.At[28]):
                self.ui.tname8.setText(f"{df.Name[28]}")
            elif current_time <= str(df.At[38]):
                self.ui.tname8.setText(f"{df.Name[38]}")
            elif current_time <= str(df.At[48]):
                self.ui.tname8.setText(f"{df.Name[48]}")
            else:
                self.ui.tname8.setText(f"{df.Name[48]}")
            if current_time <= str(df.At[9]):
                self.ui.tname9.setText(f"{df.Name[9]}")
            elif current_time <= str(df.At[19]):
                self.ui.tname9.setText(f"{df.Name[19]}")
            elif current_time <= str(df.At[29]):
                self.ui.tname9.setText(f"{df.Name[29]}")
            elif current_time <= str(df.At[39]):
                self.ui.tname9.setText(f"{df.Name[39]}")
            elif current_time <= str(df.At[49]):
                self.ui.tname9.setText(f"{df.Name[48]}")
            else:
                self.ui.tname9.setText(f"{df.Name[48]}")

            self.ui.at.setText(f"ARRIVAL TIME")
            if current_time <= str(df.At[0]):
                self.ui.at0.setText(f"{df.At[0]}")
            elif current_time <= str(df.At[10]):
                self.ui.at0.setText(f"{df.At[10]}")
            elif current_time <= str(df.At[20]):
                self.ui.at0.setText(f"{df.At[20]}")
            elif current_time <= str(df.At[30]):
                self.ui.at0.setText(f"{df.At[30]}")
            elif current_time <= str(df.At[40]):
                self.ui.at0.setText(f"{df.At[40]}")
            else:
                self.ui.at0.setText(f"00:00:00")
            if current_time <= str(df.At[1]):
                self.ui.at1.setText(f"{df.At[1]}")
            elif current_time <= str(df.At[11]):
                self.ui.at1.setText(f"{df.At[11]}")
            elif current_time <= str(df.At[21]):
                self.ui.at1.setText(f"{df.At[21]}")
            elif current_time <= str(df.At[31]):
                self.ui.at1.setText(f"{df.At[31]}")
            elif current_time <= str(df.At[41]):
                self.ui.at1.setText(f"{df.At[41]}")
            else:
                self.ui.at1.setText(f"00:00:00")
            if current_time <= str(df.At[2]):
                self.ui.at2.setText(f"{df.At[2]}")
            elif current_time <= str(df.At[12]):
                self.ui.at2.setText(f"{df.At[12]}")
            elif current_time <= str(df.At[22]):
                self.ui.at2.setText(f"{df.At[22]}")
            elif current_time <= str(df.At[32]):
                self.ui.at2.setText(f"{df.At[32]}")
            elif current_time <= str(df.At[42]):
                self.ui.at2.setText(f"{df.At[42]}")
            else:
                self.ui.at2.setText(f"00:00:00")
            if current_time <= str(df.At[3]):
                self.ui.at3.setText(f"{df.At[3]}")
            elif current_time <= str(df.At[13]):
                self.ui.at3.setText(f"{df.At[13]}")
            elif current_time <= str(df.At[23]):
                self.ui.at3.setText(f"{df.At[23]}")
            elif current_time <= str(df.At[33]):
                self.ui.at3.setText(f"{df.At[33]}")
            elif current_time <= str(df.At[43]):
                self.ui.at3.setText(f"{df.At[43]}")
            else:
                self.ui.at3.setText(f"00:00:00")
            if current_time <= str(df.At[4]):
                self.ui.at4.setText(f"{df.At[4]}")
            elif current_time <= str(df.At[14]):
                self.ui.at4.setText(f"{df.At[14]}")
            elif current_time <= str(df.At[24]):
                self.ui.at4.setText(f"{df.At[24]}")
            elif current_time <= str(df.At[34]):
                self.ui.at4.setText(f"{df.At[34]}")
            elif current_time <= str(df.At[44]):
                self.ui.at4.setText(f"{df.At[44]}")
            else:
                self.ui.at4.setText(f"{df.At[44]}")
            if current_time <= str(df.At[5]):
                self.ui.at5.setText(f"{df.At[5]}")
            elif current_time <= str(df.At[15]):
                self.ui.at5.setText(f"{df.At[15]}")
            elif current_time <= str(df.At[25]):
                self.ui.at5.setText(f"{df.At[25]}")
            elif current_time <= str(df.At[35]):
                self.ui.at5.setText(f"{df.At[35]}")
            elif current_time <= str(df.At[45]):
                self.ui.at5.setText(f"{df.At[45]}")
            else:
                self.ui.at5.setText(f"{df.At[45]}")
            if current_time <= str(df.At[6]):
                self.ui.at6.setText(f"{df.At[6]}")
            elif current_time <= str(df.At[16]):
                self.ui.at6.setText(f"{df.At[16]}")
            elif current_time <= str(df.At[26]):
                self.ui.at6.setText(f"{df.At[26]}")
            elif current_time <= str(df.At[36]):
                self.ui.at6.setText(f"{df.At[36]}")
            elif current_time <= str(df.At[46]):
                self.ui.at6.setText(f"{df.At[46]}")
            else:
                self.ui.at6.setText(f"{df.At[46]}")
            if current_time <= str(df.At[7]):
                self.ui.at7.setText(f"{df.At[7]}")
            elif current_time <= str(df.At[17]):
                self.ui.at7.setText(f"{df.At[17]}")
            elif current_time <= str(df.At[27]):
                self.ui.at7.setText(f"{df.At[27]}")
            elif current_time <= str(df.At[37]):
                self.ui.at7.setText(f"{df.At[37]}")
            elif current_time <= str(df.At[47]):
                self.ui.at7.setText(f"{df.At[47]}")
            else:
                self.ui.at7.setText(f"{df.At[47]}")
            if current_time <= str(df.At[8]):
                self.ui.at8.setText(f"{df.At[8]}")
            elif current_time <= str(df.At[18]):
                self.ui.at8.setText(f"{df.At[18]}")
            elif current_time <= str(df.At[28]):
                self.ui.at8.setText(f"{df.At[28]}")
            elif current_time <= str(df.At[38]):
                self.ui.at8.setText(f"{df.At[38]}")
            elif current_time <= str(df.At[48]):
                self.ui.at8.setText(f"{df.At[48]}")
            else:
                self.ui.at8.setText(f"{df.At[48]}")
            if current_time <= str(df.At[9]):
                self.ui.at9.setText(f"{df.At[9]}")
            elif current_time <= str(df.At[19]):
                self.ui.at9.setText(f"{df.At[19]}")
            elif current_time <= str(df.At[29]):
                self.ui.at9.setText(f"{df.At[29]}")
            elif current_time <= str(df.At[39]):
                self.ui.at9.setText(f"{df.At[39]}")
            elif current_time <= str(df.At[49]):
                self.ui.at9.setText(f"{df.At[49]}")
            else:
                self.ui.at9.setText(f"{df.At[49]}")
            self.ui.dt.setText(f"DEPARTURE TIME")
            if current_time <= str(df.At[0]):
                self.ui.dt0.setText(f"{df.Dt[0]}")
            elif current_time <= str(df.At[10]):
                self.ui.dt0.setText(f"{df.Dt[10]}")
            elif current_time <= str(df.At[20]):
                self.ui.dt0.setText(f"{df.Dt[20]}")
            elif current_time <= str(df.At[30]):
                self.ui.dt0.setText(f"{df.Dt[30]}")
            elif current_time <= str(df.At[40]):
                self.ui.dt0.setText(f"{df.Dt[40]}")
            else:
                self.ui.dt0.setText(f"00:00:00")
            if current_time <= str(df.At[1]):
                self.ui.dt1.setText(f"{df.Dt[1]}")
            elif current_time <= str(df.At[11]):
                self.ui.dt1.setText(f"{df.Dt[11]}")
            elif current_time <= str(df.At[21]):
                self.ui.dt1.setText(f"{df.Dt[21]}")
            elif current_time <= str(df.At[31]):
                self.ui.dt1.setText(f"{df.Dt[31]}")
            elif current_time <= str(df.At[41]):
                self.ui.dt1.setText(f"{df.Dt[41]}")
            else:
                self.ui.dt1.setText(f"00:00:00")
            if current_time <= str(df.At[2]):
                self.ui.dt2.setText(f"{df.Dt[2]}")
            elif current_time <= str(df.At[12]):
                self.ui.dt2.setText(f"{df.Dt[12]}")
            elif current_time <= str(df.At[22]):
                self.ui.dt2.setText(f"{df.Dt[22]}")
            elif current_time <= str(df.At[32]):
                self.ui.dt2.setText(f"{df.Dt[32]}")
            elif current_time <= str(df.At[42]):
                self.ui.dt2.setText(f"{df.Dt[42]}")
            else:
                self.ui.dt2.setText(f"00:00:00")
            if current_time <= str(df.At[3]):
                self.ui.dt3.setText(f"{df.Dt[3]}")
            elif current_time <= str(df.At[13]):
                self.ui.dt3.setText(f"{df.Dt[13]}")
            elif current_time <= str(df.At[23]):
                self.ui.dt3.setText(f"{df.Dt[23]}")
            elif current_time <= str(df.At[33]):
                self.ui.dt3.setText(f"{df.Dt[33]}")
            elif current_time <= str(df.At[43]):
                self.ui.dt3.setText(f"{df.Dt[43]}")
            else:
                self.ui.dt3.setText(f"00:00:00")
            if current_time <= str(df.At[4]):
                self.ui.dt4.setText(f"{df.Dt[4]}")
            elif current_time <= str(df.At[14]):
                self.ui.dt4.setText(f"{df.Dt[14]}")
            elif current_time <= str(df.At[24]):
                self.ui.dt4.setText(f"{df.Dt[24]}")
            elif current_time <= str(df.At[34]):
                self.ui.dt4.setText(f"{df.Dt[34]}")
            elif current_time <= str(df.At[44]):
                self.ui.dt4.setText(f"{df.Dt[44]}")
            else:
                self.ui.dt4.setText(f"{df.Dt[44]}")
            if current_time <= str(df.At[5]):
                self.ui.dt5.setText(f"{df.Dt[5]}")
            elif current_time <= str(df.At[15]):
                self.ui.dt5.setText(f"{df.Dt[15]}")
            elif current_time <= str(df.At[25]):
                self.ui.dt5.setText(f"{df.Dt[25]}")
            elif current_time <= str(df.At[35]):
                self.ui.dt5.setText(f"{df.Dt[35]}")
            elif current_time <= str(df.At[45]):
                self.ui.dt5.setText(f"{df.Dt[45]}")
            else:
                self.ui.dt5.setText(f"{df.Dt[45]}")
            if current_time <= str(df.At[6]):
                self.ui.dt6.setText(f"{df.Dt[6]}")
            elif current_time <= str(df.At[16]):
                self.ui.dt6.setText(f"{df.Dt[16]}")
            elif current_time <= str(df.At[26]):
                self.ui.dt6.setText(f"{df.Dt[26]}")
            elif current_time <= str(df.At[36]):
                self.ui.dt6.setText(f"{df.Dt[36]}")
            elif current_time <= str(df.At[46]):
                self.ui.dt6.setText(f"{df.Dt[46]}")
            else:
                self.ui.dt6.setText(f"{df.Dt[46]}")
            if current_time <= str(df.At[7]):
                self.ui.dt7.setText(f"{df.Dt[7]}")
            elif current_time <= str(df.At[17]):
                self.ui.dt7.setText(f"{df.Dt[17]}")
            elif current_time <= str(df.At[27]):
                self.ui.dt7.setText(f"{df.Dt[27]}")
            elif current_time <= str(df.At[37]):
                self.ui.dt7.setText(f"{df.Dt[37]}")
            elif current_time <= str(df.At[47]):
                self.ui.dt7.setText(f"{df.Dt[47]}")
            else:
                self.ui.dt7.setText(f"{df.Dt[47]}")
            if current_time <= str(df.At[8]):
                self.ui.dt8.setText(f"{df.Dt[8]}")
            elif current_time <= str(df.At[18]):
                self.ui.dt8.setText(f"{df.Dt[18]}")
            elif current_time <= str(df.At[28]):
                self.ui.dt8.setText(f"{df.Dt[28]}")
            elif current_time <= str(df.At[38]):
                self.ui.dt8.setText(f"{df.Dt[38]}")
            elif current_time <= str(df.At[48]):
                self.ui.dt8.setText(f"{df.Dt[48]}")
            else:
                self.ui.dt8.setText(f"{df.Dt[48]}")
            if current_time <= str(df.At[9]):
                self.ui.dt9.setText(f"{df.Dt[9]}")
            elif current_time <= str(df.At[19]):
                self.ui.dt9.setText(f"{df.Dt[19]}")
            elif current_time <= str(df.At[29]):
                self.ui.dt9.setText(f"{df.Dt[29]}")
            elif current_time <= str(df.At[39]):
                self.ui.dt9.setText(f"{df.Dt[39]}")
            elif current_time <= str(df.At[49]):
                self.ui.dt9.setText(f"{df.Dt[49]}")
            else:
                self.ui.dt9.setText(f"{df.Dt[49]}")

            self.ui.pt.setText(f"PLATFORM NO")
            if current_time <= str(df.At[0]):
                self.ui.pt0.setText(f"{df.Platform[0]}")
            elif current_time <= str(df.At[10]):
                self.ui.pt0.setText(f"{df.Platform[10]}")
            elif current_time <= str(df.At[20]):
                self.ui.pt0.setText(f"{df.Platform[20]}")
            elif current_time <= str(df.At[30]):
                self.ui.pt0.setText(f"{df.Platform[30]}")
            elif current_time <= str(df.At[40]):
                self.ui.pt0.setText(f"{df.Platform[40]}")
            else:
                self.ui.pt0.setText(f"0")
            if current_time <= str(df.At[1]):
                self.ui.pt1.setText(f"{df.Platform[1]}")
            elif current_time <= str(df.At[11]):
                self.ui.pt1.setText(f"{df.Platform[11]}")
            elif current_time <= str(df.At[21]):
                self.ui.pt1.setText(f"{df.Platform[21]}")
            elif current_time <= str(df.At[31]):
                self.ui.pt1.setText(f"{df.Platform[31]}")
            elif current_time <= str(df.At[41]):
                self.ui.pt1.setText(f"{df.Platform[41]}")
            else:
                self.ui.pt1.setText(f"0")
            if current_time <= str(df.At[2]):
                self.ui.pt2.setText(f"{df.Platform[2]}")
            elif current_time <= str(df.At[12]):
                self.ui.pt2.setText(f"{df.Platform[12]}")
            elif current_time <= str(df.At[22]):
                self.ui.pt2.setText(f"{df.Platform[22]}")
            elif current_time <= str(df.At[32]):
                self.ui.pt2.setText(f"{df.Platform[32]}")
            elif current_time <= str(df.At[42]):
                self.ui.pt2.setText(f"{df.Platform[42]}")
            else:
                self.ui.pt2.setText(f"0")
            if current_time <= str(df.At[3]):
                self.ui.pt3.setText(f"{df.Platform[3]}")
            elif current_time <= str(df.At[13]):
                self.ui.pt3.setText(f"{df.Platform[13]}")
            elif current_time <= str(df.At[23]):
                self.ui.pt3.setText(f"{df.Platform[23]}")
            elif current_time <= str(df.At[33]):
                self.ui.pt3.setText(f"{df.Platform[33]}")
            elif current_time <= str(df.At[43]):
                self.ui.pt3.setText(f"{df.Platform[43]}")
            else:
                self.ui.pt3.setText(f"0")
            if current_time <= str(df.At[4]):
                self.ui.pt4.setText(f"{df.Platform[4]}")
            elif current_time <= str(df.At[14]):
                self.ui.pt4.setText(f"{df.Platform[14]}")
            elif current_time <= str(df.At[24]):
                self.ui.pt4.setText(f"{df.Platform[24]}")
            elif current_time <= str(df.At[34]):
                self.ui.pt4.setText(f"{df.Platform[34]}")
            elif current_time <= str(df.At[44]):
                self.ui.pt4.setText(f"{df.Platform[44]}")
            else:
                self.ui.pt4.setText(f"{df.Platform[44]}")
            if current_time <= str(df.At[5]):
                self.ui.pt5.setText(f"{df.Platform[5]}")
            elif current_time <= str(df.At[15]):
                self.ui.pt5.setText(f"{df.Platform[15]}")
            elif current_time <= str(df.At[25]):
                self.ui.pt5.setText(f"{df.Platform[25]}")
            elif current_time <= str(df.At[35]):
                self.ui.pt5.setText(f"{df.Platform[35]}")
            elif current_time <= str(df.At[45]):
                self.ui.pt5.setText(f"{df.Platform[45]}")
            else:
                self.ui.pt5.setText(f"{df.Platform[45]}")
            if current_time <= str(df.At[6]):
                self.ui.pt6.setText(f"{df.Platform[6]}")
            elif current_time <= str(df.At[16]):
                self.ui.pt6.setText(f"{df.Platform[16]}")
            elif current_time <= str(df.At[26]):
                self.ui.pt6.setText(f"{df.Platform[26]}")
            elif current_time <= str(df.At[36]):
                self.ui.pt6.setText(f"{df.Platform[36]}")
            elif current_time <= str(df.At[46]):
                self.ui.pt6.setText(f"{df.Platform[46]}")
            else:
                self.ui.pt6.setText(f"{df.Platform[46]}")
            if current_time <= str(df.At[7]):
                self.ui.pt7.setText(f"{df.Platform[7]}")
            elif current_time <= str(df.At[17]):
                self.ui.pt7.setText(f"{df.Platform[17]}")
            elif current_time <= str(df.At[27]):
                self.ui.pt7.setText(f"{df.Platform[27]}")
            elif current_time <= str(df.At[37]):
                self.ui.pt7.setText(f"{df.Platform[37]}")
            elif current_time <= str(df.At[47]):
                self.ui.pt7.setText(f"{df.Platform[47]}")
            else:
                self.ui.pt7.setText(f"{df.Platform[47]}")
            if current_time <= str(df.At[8]):
                self.ui.pt8.setText(f"{df.Platform[8]}")
            elif current_time <= str(df.At[18]):
                self.ui.pt8.setText(f"{df.Platform[18]}")
            elif current_time <= str(df.At[28]):
                self.ui.pt8.setText(f"{df.Platform[28]}")
            elif current_time <= str(df.At[38]):
                self.ui.pt8.setText(f"{df.Platform[38]}")
            elif current_time <= str(df.At[48]):
                self.ui.pt8.setText(f"{df.Platform[48]}")
            else:
                self.ui.pt8.setText(f"{df.Platform[48]}")
            if current_time <= str(df.At[9]):
                self.ui.pt9.setText(f"{df.Platform[9]}")
            elif current_time <= str(df.At[19]):
                self.ui.pt9.setText(f"{df.Platform[19]}")
            elif current_time <= str(df.At[29]):
                self.ui.pt9.setText(f"{df.Platform[29]}")
            elif current_time <= str(df.At[39]):
                self.ui.pt9.setText(f"{df.Platform[39]}")
            elif current_time <= str(df.At[49]):
                self.ui.pt9.setText(f"{df.Platform[49]}")
            else:
                self.ui.pt9.setText(f"{df.Platform[49]}")

            QApplication.processEvents()










if __name__ == "__main__":
    app =QApplication(sys.argv)
    w=MyForm1()
    w.show()
    sys.exit(app.exec_())