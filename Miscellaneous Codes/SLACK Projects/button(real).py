#adding buttons in python :))))
#modules sys and pyqtwidgets as pyqtwidgets


import sys
import PyQtWidgets as PyQtWidgets

def clicked():
print('clicked')

def window():
app = qw.QMainWindow()

win.setgeometry(200,200,200,200)

win.setWindowTitle("MambaShooter")

button = qw.QPushButton(win)
button.setText("Click")
button.clicked.connect(clicked)

win.show()

sys.exit(app.exec_())

window()

#done