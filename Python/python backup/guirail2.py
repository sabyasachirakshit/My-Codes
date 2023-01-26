import sys
import os
import pandas as pd
from PyQt5.QtWidgets import QMainWindow,QApplication
from afridip2 import *
import time
from datetime import datetime
df = pd.read_excel("raildata.xlsx")
class MyForm2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.details.clicked.connect(self.details)
        self.show()


    def details(self):
        while True:
            QApplication.processEvents()
            localtime1 = time.asctime(time.localtime(time.time()))
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.ui.dc.setText(f"INDIAN RAILWAYS         {localtime1}         INDIAN RAILWAYS")
            a1=self.ui.dropdown.currentText()
            i = 0
            while (i < 50):
                QApplication.processEvents()
                if a1 == f"{df.Train[i]}    {df.Name[i]}":
                    self.ui.tn0.setText(f" {df.Train[i]}")
                    self.ui.tname0.setText(f" {df.Name[i]}")
                    self.ui.at0.setText(f" {df.At[i]}")
                    self.ui.dt0.setText(f" {df.Dt[i]}")
                    self.ui.pt0.setText(f" {df.Platform[i]}")
                    if current_time<str(df.Ant_Time[i]):
                        self.ui.an0.setText(f" The Train Announcement Has Not Been Done Yet.")
                    elif current_time>str(df.At[i]):
                        self.ui.an0.setText(f" The Train Announcement Has Been Done.")
                    elif current_time>=str(df.Ant_Time[i]) and current_time<str(df.At[i]):
                        self.ui.an0.setText(f" The Train Announcement Is Being Done Now.")

                i += 1


if __name__ == "__main__":
    app =QApplication(sys.argv)
    w=MyForm2()
    w.show()
    sys.exit(app.exec_())