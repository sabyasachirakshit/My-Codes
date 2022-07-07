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
            if a1 == f"{df.Train[0]}    {df.Name[0]}":
                i=0

                while(i<8):
                    QApplication.processEvents()
                    if current_time>str(df1.S_Time1[i]) and current_time<str(df1.S_Time1[i+1]) and i==0:
                       self.ui.display.setText(f"Train No - {df.Train[0]}   {df.Name[0]} \nHas Left {df1.Train1[0]} at {df1.S_Time1[0]}\n And Will Be Arriving {df1.Train1[1]} At {df1.S_Time1[1]} 1loop{i}")
                       break
                    elif current_time > str(df1.S_Time1[i]) and current_time < str(df1.S_Time1[i + 1]) and weekday1 == 0:
                        self.ui.display.setText(f"Train No - {df.Train[0]}   {df.Name[0]} \nHas Reached {df1.Train1[i]} At {df1.S_Time1[i]}\n And Will Be Arriving {df1.Train1[i+1]} At {df1.S_Time1[i+1]} 2loop{i}")
                        break
                    elif current_time>str(df1.S_Time1[i]) and current_time<str(df1.S_Time1[i+1]) and weekday1==1:
                        self.ui.display.setText(f"Train No - {df.Train[0]}   {df.Name[0]} \nHas Reached {df1.Train1[i]} At {df1.S_Time1[i]}\n And Will Be Arriving {df1.Train1[i+1]} At {df1.S_Time1[i+1]} 3loop{i}")
                        break
                    elif current_time<=str(df1.S_Time1[0]) and weekday1==0:
                        self.ui.display.setText(f"Train No - {df.Train[0]}   {df.Name[0]} \nIs Cuurently In {df1.Train1[0]}\nAnd Will Be Left {df1.Train1[0]} At {df1.S_Time1[0]} \nAnd Will Be Arriving {df1.Train1[1]} At {df1.S_Time1[1]} 4loop{i}")
                        break
                    elif current_time>= str(df1.S_Time1[8]) and weekday1==1:
                        self.ui.display.setText(f"Train No - {df.Train[0]}   {df.Name[0]} \nHas Reached {df1.Train1[8]} At {df1.S_Time1[8]} 5loop{i}")
                        break
                    elif current_time>str(df1.S_Time1[i]) and current_time>str(df1.S_Time1[i+1]) and df1.Wkd1[i+1]==1 and current_time>str(df1.S_Time1[0]):
                        self.ui.display.setText(f"Train No - {df.Train[0]}   {df.Name[0]} \nHas Reached {df1.Train1[i]} At {df1.S_Time1[i]}\n And Will Be Arriving {df1.Train1[i+1]} At {df1.S_Time1[i+1]} 6loop{i}")
                        break
                    elif current_time<str(df1.S_Time1[i]) and current_time<str(df1.S_Time1[i+1]) and df1.Wkd1[i+1]==1:
                        self.ui.display.setText(f"Train No - {df.Train[0]}   {df.Name[0]} \nHas Reached {df1.Train1[i]} At {df1.S_Time1[i]}\n And Will Be Arriving {df1.Train1[i + 1]} At {df1.S_Time1[i + 1]} 7loop{i}")
                        break
                    i+=1



            # elif a1 == f"{df.Train[4]}    {df.Name[4]}":
            #     i1=0
            #     while(i1<22):
            #         if current_time > str(df1.S_Time5[i1]) and current_time < str(df1.S_Time5[i1 + 1]) and weekday1 == df1.Wkd5[i1]:
            #             self.ui.display.setText(f"Train No - {df.Train[4]}   {df.Name[4]} \nHas Reached {df1.Train5[i1]} At {df1.S_Time5[i1]}\n And Will Be Arriving {df1.Train5[i1 + 1]} At {df1.S_Time5[i1 + 1]}")
            #         elif current_time <= str(df1.S_Time5[0]) and weekday1 == df1.Wkd5[0]:
            #             self.ui.display.setText(f"Train No - {df.Train[4]}   {df.Name[4]} \nIs Cuurently In {df1.Train5[0]}\n And Will Be Arriving {df1.Train5[1]} At {df1.S_Time5[1]}")
            #         elif current_time >= str(df1.S_Time5[22]) and weekday1 == df1.Wkd5[22]:
            #             self.ui.display.setText(f"Train No - {df.Train[4]}   {df.Name[4]} \nHas Reached {df1.Train5[22]} At {df1.S_Time5[22]}")
            #         elif current_time > str(df1.S_Time5[i1]) and current_time > str(df1.S_Time5[i1+ 1]) and weekday1==df1.Wkd5[i1-1]:
            #             self.ui.display.setText(f"Train No - {df1.Train[4]}   {df.Name[4]} \nHas Reached {df1.Train5[i1]} At {df1.S_Time5[i1]}\n And Will Be Arriving {df1.Train5[i1 + 1]} At {df1.S_Time1[i1 + 1]}")
            #         elif weekday1 == df1.Wkd5[i1] and current_time <str(df1.S_Time5[i1]) and current_time < str(df1.S_Time5[i1 + 1]):
            #             self.ui.display.setText(f"Train No - {df.Train[4]}   {df.Name[4]} \nHas Reached {df1.Train5[i1]} At {df1.S_Time5[i1]}\n And Will Be Arriving {df1.Train5[i1 + 1]} At {df1.S_Time1[i1 + 1]}")
            #         # elif weekday1 == df1.Wkd5[i1 + 1] and current_time < str(df1.S_Time5[i1]) and current_time < str(df1.S_Time1[i1 + 1]):
            #         #     self.ui.display.setText(f"Train No - {df.Train[4]}   {df.Name[4]} \nHas Reached {df1.Train5[i1]} At {df1.S_Time5[i1]}\n And Will Be Arriving {df1.Train5[i1 + 1]} At {df1.S_Time1[i1 + 1]}")
            #     i1 += 1



if __name__ == "__main__":
    app =QApplication(sys.argv)
    w=MyForm3()
    w.show()
    sys.exit(app.exec_())