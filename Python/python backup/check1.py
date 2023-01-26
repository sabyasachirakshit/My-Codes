import sys
import pandas as pd
df=pd.read_excel("raildata.xlsx")
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
            self.ui.tname.setText(f"TRAIN NAME")
            self.ui.at.setText(f"ARRIVAL TIME")
            self.ui.dt.setText(f"DEPARTURE TIME")
            self.ui.pt.setText(f"PLATFORM NO")
            i1=0
            i=0
            j=1
            k=2
            l=3
            m=4
            n=5
            o=6
            p=7
            q=8
            r=9
            while(i1<10):
                if current_time <= str(df.At[i]):
                    self.ui.tn0.setText(f"{df.Train[i]}")
                    self.ui.tname0.setText(f"{df.Name[i]}")
                    self.ui.at0.setText(f"{df.At[i]}")
                    self.ui.dt0.setText(f"{df.Dt[i]}")
                    self.ui.pt0.setText(f"{df.Platform[i]}")

                if current_time <= str(df.At[j]):
                    self.ui.tn1.setText(f"{df.Train[j]}")
                    self.ui.tname1.setText(f"{df.Name[j]}")
                    self.ui.at1.setText(f"{df.At[j]}")
                    self.ui.dt1.setText(f"{df.Dt[j]}")
                    self.ui.pt1.setText(f"{df.Platform[j]}")

                if current_time <= str(df.At[k]):
                    self.ui.tn2.setText(f"{df.Train[k]}")
                    self.ui.tname2.setText(f"{df.Name[k]}")
                    self.ui.at2.setText(f"{df.At[k]}")
                    self.ui.dt2.setText(f"{df.Dt[k]}")
                    self.ui.pt2.setText(f"{df.Platform[k]}")

                if current_time <= str(df.At[l]):
                    self.ui.tn3.setText(f"{df.Train[l]}")
                    self.ui.tname3.setText(f"{df.Name[l]}")
                    self.ui.at3.setText(f"{df.At[l]}")
                    self.ui.dt3.setText(f"{df.Dt[l]}")
                    self.ui.pt3.setText(f"{df.Platform[l]}")

                if current_time <= str(df.At[m]):
                    self.ui.tn4.setText(f"{df.Train[m]}")
                    self.ui.tname4.setText(f"{df.Name[m]}")
                    self.ui.at4.setText(f"{df.At[m]}")
                    self.ui.dt4.setText(f"{df.Dt[m]}")
                    self.ui.pt4.setText(f"{df.Platform[m]}")

                if current_time <= str(df.At[n]):
                    self.ui.tn5.setText(f"{df.Train[n]}")
                    self.ui.tname5.setText(f"{df.Name[n]}")
                    self.ui.at5.setText(f"{df.At[n]}")
                    self.ui.dt5.setText(f"{df.Dt[n]}")
                    self.ui.pt5.setText(f"{df.Platform[n]}")

                if current_time <= str(df.At[o]):
                    self.ui.tn6.setText(f"{df.Train[o]}")
                    self.ui.tname6.setText(f"{df.Name[o]}")
                    self.ui.at6.setText(f"{df.At[o]}")
                    self.ui.dt6.setText(f"{df.Dt[o]}")
                    self.ui.pt6.setText(f"{df.Platform[o]}")

                if current_time <= str(df.At[p]):
                    self.ui.tn7.setText(f"{df.Train[p]}")
                    self.ui.tname7.setText(f"{df.Name[p]}")
                    self.ui.at7.setText(f"{df.At[p]}")
                    self.ui.dt7.setText(f"{df.Dt[p]}")
                    self.ui.pt7.setText(f"{df.Platform[p]}")

                if current_time <= str(df.At[q]):
                    self.ui.tn8.setText(f"{df.Train[q]}")
                    self.ui.tname8.setText(f"{df.Name[q]}")
                    self.ui.at8.setText(f"{df.At[q]}")
                    self.ui.dt8.setText(f"{df.Dt[q]}")
                    self.ui.pt8.setText(f"{df.Platform[q]}")

                if current_time <= str(df.At[r]):
                    self.ui.tn9.setText(f"{df.Train[r]}")
                    self.ui.tname9.setText(f"{df.Name[r]}")
                    self.ui.at9.setText(f"{df.At[r]}")
                    self.ui.dt9.setText(f"{df.Dt[r]}")
                    self.ui.pt9.setText(f"{df.Platform[r]}")

                i1+=1
                i+=10
                j+=10
                k+=10
                l+=10
                m+=10
                n+=10
                o+=10
                p+=10
                q+=10
                r+=10
                QApplication.processEvents()
            self.ui.tn0.setText(f"0   0   0   0   0 ")
            self.ui.tname0.setText(f"Welcome To Indian Railways ")
            self.ui.at0.setText(f"00:00:00")
            self.ui.dt0.setText(f"00:00:00")
            self.ui.pt0.setText(f"0")

            self.ui.tn1.setText(f"0   0   0   0   0 ")
            self.ui.tname1.setText(f"Welcome To Indian Railways ")
            self.ui.at1.setText(f"00:00:00")
            self.ui.dt1.setText(f"00:00:00")
            self.ui.pt1.setText(f"0")

            self.ui.tn2.setText(f"0   0   0   0   0 ")
            self.ui.tname2.setText(f"Welcome To Indian Railways ")
            self.ui.at2.setText(f"00:00:00")
            self.ui.dt2.setText(f"00:00:00")
            self.ui.pt2.setText(f"0")

            self.ui.tn3.setText(f"0   0   0   0   0 ")
            self.ui.tname3.setText(f"Welcome To Indian Railways ")
            self.ui.at3.setText(f"00:00:00")
            self.ui.dt3.setText(f"00:00:00")
            self.ui.pt3.setText(f"0")

            self.ui.tn4.setText(f"{df.Train[44]}")
            self.ui.tname4.setText(f"{df.Name[44]}")
            self.ui.at4.setText(f"{df.At[44]}")
            self.ui.dt4.setText(f"{df.Dt[44]}")
            self.ui.pt4.setText(f"{df.Platform[44]}")

            self.ui.tn5.setText(f"{df.Train[45]}")
            self.ui.tname5.setText(f"{df.Name[45]}")
            self.ui.at5.setText(f"{df.At[45]}")
            self.ui.dt5.setText(f"{df.Dt[45]}")
            self.ui.pt5.setText(f"{df.Platform[45]}")

            self.ui.tn6.setText(f"{df.Train[46]}")
            self.ui.tname6.setText(f"{df.Name[46]}")
            self.ui.at6.setText(f"{df.At[46]}")
            self.ui.dt6.setText(f"{df.Dt[46]}")
            self.ui.pt6.setText(f"{df.Platform[46]}")

            self.ui.tn7.setText(f"{df.Train[47]}")
            self.ui.tname7.setText(f"{df.Name[47]}")
            self.ui.at7.setText(f"{df.At[47]}")
            self.ui.dt7.setText(f"{df.Dt[47]}")
            self.ui.pt7.setText(f"{df.Platform[47]}")

            self.ui.tn8.setText(f"{df.Train[48]}")
            self.ui.tname8.setText(f"{df.Name[48]}")
            self.ui.at8.setText(f"{df.At[48]}")
            self.ui.dt8.setText(f"{df.Dt[48]}")
            self.ui.pt8.setText(f"{df.Platform[48]}")

            self.ui.tn9.setText(f"{df.Train[49]}")
            self.ui.tname9.setText(f"{df.Name[49]}")
            self.ui.at9.setText(f"{df.At[49]}")
            self.ui.dt9.setText(f"{df.Dt[49]}")
            self.ui.pt9.setText(f"{df.Platform[49]}")

            QApplication.processEvents()


    def locationdisplay(self):
        self.w = MyForm3()
        self.w.show()
    def statusdisplay(self):
        self.w = MyForm2()
        self.w.show()

if __name__ == "__main__":
    app =QApplication(sys.argv)
    w=MyForm1()
    w.show()
    sys.exit(app.exec_())