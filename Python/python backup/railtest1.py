# ae88c1141e41bb3cfe8a059c94deba05    api key
# cb8f7317eb556eff2cf75fa15879a9f2  private key
# http://indianrailapi.com/api/v2/livetrainstatus/apikey/<apikey>/trainnumber/<train_number>/date/<yyyymmdd>/
# http://indianrailapi.com/api/v2/LiveStation/apikey/<apikey>/StationCode/<StationCode>/hours/<Hours>/
# def announce():
#     import pandas as pd
#     import time
#     from datetime import datetime
#     df = pd.read_excel("raildata.xlsx")
#     print(df)
#
#     def railstatus1(filename):
#         df = pd.read_excel(filename)
#         print(
#             f" Train No - {df.Train[0]} \n Train Name - {df.Name[0]}\n From - {df.From[0]} \n Via - {df.Via[0]} \n To - {df.To[0]} \n Platform No - {df.Platform[0]} \n Time - {df.Time[0]}")
#
#     def railstatus2(filename):
#         df = pd.read_excel(filename)
#         print(
#             f" Train No - {df.Train[1]} \n Train Name - {df.Name[1]}\n From - {df.From[1]} \n Via - {df.Via[1]} \n To - {df.To[1]} \n Platform No - {df.Platform[1]} \n Time - {df.Time[1]}")
#
#     Time0 = df.Time[0]
#     Time1 = df.Time[1]
#
#     while True:
#         localtime1 = time.asctime(time.localtime(time.time()))
#         now = datetime.now()
#         current_time = now.strftime("%H:%M:%S")
#         if current_time == str(Time0):
#             railstatus1("raildata.xlsx")
#             time.sleep(1)
#         elif current_time == str(Time1):
#             railstatus2("raildata.xlsx")
#             time.sleep(1)
#
# announce()
import sys
import pygame
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
        import pandas as pd
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

        Time0 = df.Time[0]
        Time1 = df.Time[1]

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
                pygame.mixer.music.load("1   2   1   3   0_English.mp3")
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play(3)









if __name__ == "__main__":
    app =QApplication(sys.argv)
    w=MyForm()
    w.show()
    sys.exit(app.exec_())