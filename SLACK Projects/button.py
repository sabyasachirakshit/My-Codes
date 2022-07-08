#adding buttons in python :))))
#modules sys and pyqtwidgets as pyqtwidgets


import sys
from PyQt5 import QtWidgets as qw

def clicked():
    print('clicked')

def window():
    global app
    app = qw.QMainWindow()


button = qw.QPushButton(window)

button.setgeometry(200,200,200,200)

button.setWindowTitle("MambaShooter")
button.setText("Click")
button.clicked.connect(clicked)
window()
window.show()

sys.exit(app.exec_())



#done