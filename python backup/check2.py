import sys
import pandas as pd
from PyQt5.QtWidgets import QMainWindow,QApplication
from afridip3 import *
import time
from datetime import datetime
df = pd.read_excel("raildata.xlsx")
df1= pd.read_excel("rail_data2.xlsx")
class MyForm3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.location.clicked.connect(self.details)
        self.show()

    def details(self):
        while True:
            QApplication.processEvents()
            localtime1 = time.asctime(time.localtime(time.time()))
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            weekday1=datetime.today().weekday()
            self.ui.clock.setText(f"INDIAN RAILWAYS         {localtime1}        INDIAN RAILWAYS")
            a1=self.ui.dropdown.currentText()
            i1=0
            while(i1<101):
                QApplication.processEvents()
                if a1 == f"{df.Train[i1]}    {df.Name[i1]}":
                    i=0

                    def func1(n):
                        if n == 0:
                            return df1.Train1
                        elif n == 1:
                            return df1.Train2
                        elif n == 2:
                            return df1.Train3
                        elif n == 3:
                            return df1.Train4
                        elif n == 4:
                            return df1.Train5
                        elif n == 5:
                            return df1.Train6
                        elif n == 6:
                            return df1.Train7
                        elif n == 7:
                            return df1.Train8
                        elif n == 8:
                            return df1.Train9
                        elif n == 9:
                            return df1.Train10
                        elif n == 10:
                            return df1.Train11
                        elif n == 11:
                            return df1.Train12
                        elif n == 12:
                            return df1.Train13
                        elif n == 13:
                            return df1.Train14
                        elif n == 14:
                            return df1.Train15
                        elif n == 15:
                            return df1.Train16
                        elif n == 16:
                            return df1.Train17
                        elif n == 17:
                            return df1.Train18
                        elif n == 18:
                            return df1.Train19
                        elif n == 19:
                            return df1.Train20
                        elif n == 20:
                            return df1.Train21
                        elif n == 21:
                            return df1.Train22
                        elif n == 22:
                            return df1.Train23
                        elif n == 23:
                            return df1.Train24
                        elif n == 24:
                            return df1.Train25
                        elif n == 25:
                            return df1.Train26
                        elif n == 26:
                            return df1.Train27
                        elif n == 27:
                            return df1.Train28
                        elif n == 28:
                            return df1.Train29
                        elif n == 29:
                            return df1.Train30
                        elif n == 30:
                            return df1.Train31
                        elif n == 31:
                            return df1.Train32
                        elif n == 32:
                            return df1.Train33
                        elif n == 33:
                            return df1.Train34
                        elif n == 34:
                            return df1.Train35
                        elif n == 35:
                            return df1.Train36
                        elif n == 36:
                            return df1.Train37
                        elif n == 37:
                            return df1.Train38
                        elif n == 38:
                            return df1.Train39
                        elif n == 39:
                            return df1.Train40
                        elif n == 40:
                            return df1.Train41
                        elif n == 41:
                            return df1.Train42
                        elif n == 42:
                            return df1.Train43
                        elif n == 43:
                            return df1.Train44
                        elif n == 44:
                            return df1.Train45
                        elif n == 45:
                            return df1.Train46
                        elif n == 46:
                            return df1.Train47
                        elif n == 47:
                            return df1.Train48
                        elif n == 48:
                            return df1.Train49
                        elif n == 49:
                            return df1.Train50
                    functrain=func1(i1)
                    def func2(n):
                        if n == 0:
                            return df1.S_Time1
                        elif n == 1:
                            return df1.S_Time2
                        elif n == 2:
                            return df1.S_Time3
                        elif n == 3:
                            return df1.S_Time4
                        elif n == 4:
                            return df1.S_Time5
                        elif n == 5:
                            return df1.S_Time6
                        elif n == 6:
                            return df1.S_Time7
                        elif n == 7:
                            return df1.S_Time8
                        elif n == 8:
                            return df1.S_Time9
                        elif n == 9:
                            return df1.S_Time10
                        elif n == 10:
                            return df1.S_Time11
                        elif n == 11:
                            return df1.S_Time12
                        elif n == 12:
                            return df1.S_Time13
                        elif n == 13:
                            return df1.S_Time14
                        elif n == 14:
                            return df1.S_Time15
                        elif n == 15:
                            return df1.S_Time16
                        elif n == 16:
                            return df1.S_Time17
                        elif n == 17:
                            return df1.S_Time18
                        elif n == 18:
                            return df1.S_Time19
                        elif n == 19:
                            return df1.S_Time20
                        elif n == 20:
                            return df1.S_Time21
                        elif n == 21:
                            return df1.S_Time22
                        elif n == 22:
                            return df1.S_Time23
                        elif n == 23:
                            return df1.S_Time24
                        elif n == 24:
                            return df1.S_Time25
                        elif n == 25:
                            return df1.S_Time26
                        elif n == 26:
                            return df1.S_Time27
                        elif n == 27:
                            return df1.S_Time28
                        elif n == 28:
                            return df1.S_Time29
                        elif n == 29:
                            return df1.S_Time30
                        elif n == 30:
                            return df1.S_Time31
                        elif n == 31:
                            return df1.S_Time32
                        elif n == 32:
                            return df1.S_Time33
                        elif n == 33:
                            return df1.S_Time34
                        elif n == 34:
                            return df1.S_Time35
                        elif n == 35:
                            return df1.S_Time36
                        elif n == 36:
                            return df1.S_Time37
                        elif n == 37:
                            return df1.S_Time38
                        elif n == 38:
                            return df1.S_Time39
                        elif n == 39:
                            return df1.S_Time40
                        elif n == 40:
                            return df1.S_Time41
                        elif n == 41:
                            return df1.S_Time42
                        elif n == 42:
                            return df1.S_Time43
                        elif n == 43:
                            return df1.S_Time44
                        elif n == 44:
                            return df1.S_Time45
                        elif n == 45:
                            return df1.S_Time46
                        elif n == 46:
                            return df1.S_Time47
                        elif n == 47:
                            return df1.S_Time48
                        elif n == 48:
                            return df1.S_Time49
                        elif n == 49:
                            return df1.S_Time50
                    funcstation=func2(i1)
                    def func3(n):
                        if n == 0:
                            return df1.Wkd1
                        elif n == 1:
                            return df1.Wkd2
                        elif n == 2:
                            return df1.Wkd3
                        elif n == 3:
                            return df1.Wkd4
                        elif n == 4:
                            return df1.Wkd5
                    funcweek=func3(i1)
                    while(i<60):
                        QApplication.processEvents()
                        if current_time>str(funcstation[i]) and current_time<str(funcstation[i+1]) and i==0:
                           self.ui.display.setText(f"Train No - {df.Train[i1]}   {df.Name[i1]} \nHas Left {functrain[0]} at {funcstation[0]}\n And Will Be Arriving {functrain[1]} At {funcstation[1]}")
                           break
                        elif current_time > str(funcstation[i]) and current_time < str(funcstation[i + 1]) and weekday1 == 0:
                            self.ui.display.setText(f"Train No - {df.Train[i1]}   {df.Name[i1]} \nHas Reached {functrain[i]} At {funcstation[i]}\n And Will Be Arriving {functrain[i+1]} At {funcstation[i+1]}")
                            break
                        elif current_time>str(funcstation[i]) and current_time<str(funcstation[i+1]) and weekday1==1:
                            self.ui.display.setText(f"Train No - {df.Train[i1]}   {df.Name[i1]} \nHas Reached {functrain[i]} At {funcstation[i]}\n And Will Be Arriving {functrain[i+1]} At {funcstation[i+1]} ")
                            break
                        elif current_time<=str(funcstation[0]) and weekday1==0:
                            self.ui.display.setText(f"Train No - {df.Train[i1]}   {df.Name[i1]} \nIs Cuurently In {functrain[0]}\nAnd Will Be Left {functrain[0]} At {funcstation[0]} \nAnd Will Be Arriving {functrain[1]} At {funcstation[1]}")
                            break
                        elif current_time>= str(funcstation[8]) and weekday1==1:
                            self.ui.display.setText(f"Train No - {df.Train[i1]}   {df.Name[i1]} \nHas Reached {functrain[8]} At {funcstation[8]}")
                            break
                        elif current_time>str(funcstation[i]) and current_time>str(funcstation[i+1]) and funcweek[i+1]==1 and current_time>str(funcstation[0]):
                            self.ui.display.setText(f"Train No - {df.Train[i1]}   {df.Name[i1]} \nHas Reached {functrain[i]} At {funcstation[i]}\n And Will Be Arriving {functrain[i+1]} At {funcstation[i+1]} ")
                            break
                        elif current_time<str(funcstation[i]) and current_time<str(funcstation[i+1]) and funcweek[i+1]==1:
                            self.ui.display.setText(f"Train No - {df.Train[i1]}   {df.Name[i1]} \nHas Reached {functrain[i]} At {funcstation[i]}\n And Will Be Arriving {functrain[i + 1]} At {funcstation[i + 1]} ")
                            break
                        i+=1
                    break
                i1+=1



               


if __name__ == "__main__":
    app =QApplication(sys.argv)
    w=MyForm3()
    w.show()
    sys.exit(app.exec_())