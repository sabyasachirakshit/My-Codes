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
            pygame.mixer.init()
            QApplication.processEvents()
            localtime1 = time.asctime(time.localtime(time.time()))
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.ui.clock.setText(f"{localtime1}")
            if current_time == str(Time0):
                railstatus1("raildata.xlsx")
                pygame.mixer.music.load("announceHindi_3---6---8---1---1_1.mp3")
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play(1)
                time.sleep(20)
                pygame.mixer.music.load("announcement_3---6---8---1---1_1.mp3")
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play(1)
                time.sleep(20)

            elif current_time == str(Time1):
                railstatus2("raildata.xlsx")








if __name__ == "__main__":
    app =QApplication(sys.argv)
    w=MyForm()
    w.show()
    sys.exit(app.exec_())