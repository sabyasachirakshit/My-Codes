# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'afridip2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1157, 794)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.dropdown.setGeometry(QtCore.QRect(260, 50, 621, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 54, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(161, 31, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 54, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 246))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        self.dropdown.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dropdown.setFont(font)
        self.dropdown.setMouseTracking(False)
        self.dropdown.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.dropdown.setAcceptDrops(False)
        self.dropdown.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dropdown.setAutoFillBackground(True)
        self.dropdown.setStyleSheet("")
        self.dropdown.setEditable(True)
        self.dropdown.setIconSize(QtCore.QSize(16, 16))
        self.dropdown.setDuplicatesEnabled(False)
        self.dropdown.setFrame(True)
        self.dropdown.setObjectName("dropdown")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dc = QtWidgets.QLabel(self.centralwidget)
        self.dc.setGeometry(QtCore.QRect(260, 290, 831, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dc.setFont(font)
        self.dc.setStyleSheet("color:#ca0508;\n"
"background-color:#191919;\n"
"border-style:outset;\n"
"border-color:#aa0000;\n"
"border-width:4px;\n"
"border-radius:8px")
        self.dc.setText("")
        self.dc.setAlignment(QtCore.Qt.AlignCenter)
        self.dc.setObjectName("dc")
        self.tn = QtWidgets.QLabel(self.centralwidget)
        self.tn.setGeometry(QtCore.QRect(260, 350, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tn.setFont(font)
        self.tn.setStyleSheet("color:#ca0508;\n"
"background-color:#191919;\n"
"border-style:outset;\n"
"border-color:#aa0000;\n"
"border-width:3px;\n"
"border-radius:6px")
        self.tn.setAlignment(QtCore.Qt.AlignCenter)
        self.tn.setObjectName("tn")
        self.tname = QtWidgets.QLabel(self.centralwidget)
        self.tname.setGeometry(QtCore.QRect(260, 400, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tname.setFont(font)
        self.tname.setStyleSheet("color:#ca0508;\n"
"background-color:#191919;\n"
"border-style:outset;\n"
"border-color:#aa0000;\n"
"border-width:3px;\n"
"border-radius:6px")
        self.tname.setAlignment(QtCore.Qt.AlignCenter)
        self.tname.setObjectName("tname")
        self.at = QtWidgets.QLabel(self.centralwidget)
        self.at.setGeometry(QtCore.QRect(260, 450, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.at.setFont(font)
        self.at.setStyleSheet("color:#ca0508;\n"
"background-color:#191919;\n"
"border-style:outset;\n"
"border-color:#aa0000;\n"
"border-width:3px;\n"
"border-radius:6px")
        self.at.setAlignment(QtCore.Qt.AlignCenter)
        self.at.setObjectName("at")
        self.dt = QtWidgets.QLabel(self.centralwidget)
        self.dt.setGeometry(QtCore.QRect(260, 500, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dt.setFont(font)
        self.dt.setStyleSheet("color:#ca0508;\n"
"background-color:#191919;\n"
"border-style:outset;\n"
"border-color:#aa0000;\n"
"border-width:3px;\n"
"border-radius:6px")
        self.dt.setAlignment(QtCore.Qt.AlignCenter)
        self.dt.setObjectName("dt")
        self.pt = QtWidgets.QLabel(self.centralwidget)
        self.pt.setGeometry(QtCore.QRect(260, 550, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pt.setFont(font)
        self.pt.setStyleSheet("color:#ca0508;\n"
"background-color:#191919;\n"
"border-style:outset;\n"
"border-color:#aa0000;\n"
"border-width:3px;\n"
"border-radius:6px")
        self.pt.setAlignment(QtCore.Qt.AlignCenter)
        self.pt.setObjectName("pt")
        self.an = QtWidgets.QLabel(self.centralwidget)
        self.an.setGeometry(QtCore.QRect(260, 600, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.an.setFont(font)
        self.an.setStyleSheet("color:#ca0508;\n"
"background-color:#191919;\n"
"border-style:outset;\n"
"border-color:#aa0000;\n"
"border-width:3px;\n"
"border-radius:6px")
        self.an.setAlignment(QtCore.Qt.AlignCenter)
        self.an.setObjectName("an")
        self.tn0 = QtWidgets.QLabel(self.centralwidget)
        self.tn0.setGeometry(QtCore.QRect(480, 350, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tn0.setFont(font)
        self.tn0.setStyleSheet("color:white;\n"
"background-color:#191919;\n"
"border-style:outset;\n"
"border-color:#aa0000;\n"
"border-width:3px;\n"
"border-radius:6px")
        self.tn0.setText("")
        self.tn0.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tn0.setObjectName("tn0")
        self.tname0 = QtWidgets.QLabel(self.centralwidget)
        self.tname0.setGeometry(QtCore.QRect(480, 400, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tname0.setFont(font)
        self.tname0.setStyleSheet("color:white;\n"
"background-color:#191919;\n"
"border-style:outset;\n"
"border-color:#aa0000;\n"
"border-width:3px;\n"
"border-radius:6px")
        self.tname0.setText("")
        self.tname0.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tname0.setObjectName("tname0")
        self.at0 = QtWidgets.QLabel(self.centralwidget)
        self.at0.setGeometry(QtCore.QRect(480, 450, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.at0.setFont(font)
        self.at0.setStyleSheet("color:white;\n"
"background-color:#191919;\n"
"border-style:outset;\n"
"border-color:#aa0000;\n"
"border-width:3px;\n"
"border-radius:6px")
        self.at0.setText("")
        self.at0.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.at0.setObjectName("at0")
        self.dt0 = QtWidgets.QLabel(self.centralwidget)
        self.dt0.setGeometry(QtCore.QRect(480, 500, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dt0.setFont(font)
        self.dt0.setStyleSheet("color:white;\n"
"background-color:#191919;\n"
"border-style:outset;\n"
"border-color:#aa0000;\n"
"border-width:3px;\n"
"border-radius:6px")
        self.dt0.setText("")
        self.dt0.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dt0.setObjectName("dt0")
        self.pt0 = QtWidgets.QLabel(self.centralwidget)
        self.pt0.setGeometry(QtCore.QRect(480, 550, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pt0.setFont(font)
        self.pt0.setStyleSheet("color:white;\n"
"background-color:#191919;\n"
"border-style:outset;\n"
"border-color:#aa0000;\n"
"border-width:3px;\n"
"border-radius:6px")
        self.pt0.setText("")
        self.pt0.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pt0.setObjectName("pt0")
        self.an0 = QtWidgets.QLabel(self.centralwidget)
        self.an0.setGeometry(QtCore.QRect(480, 600, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.an0.setFont(font)
        self.an0.setStyleSheet("color:white;\n"
"background-color:#191919;\n"
"border-style:outset;\n"
"border-color:#aa0000;\n"
"border-width:3px;\n"
"border-radius:6px")
        self.an0.setText("")
        self.an0.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.an0.setObjectName("an0")
        self.details = QtWidgets.QPushButton(self.centralwidget)
        self.details.setGeometry(QtCore.QRect(910, 50, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.details.setFont(font)
        self.details.setStyleSheet("background-color:rgb(33, 33, 33);\n"
"border-color::rgb(0, 170, 0);\n"
"border-width:5px;\n"
"border-radius:8px;\n"
"color:white;")
        self.details.setObjectName("details")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1157, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dropdown.setItemText(0, _translate("MainWindow", "1   2   8   8   1    Puri---Garib---Rath---Express"))
        self.dropdown.setItemText(1, _translate("MainWindow", "1   2   1   3   0    Azad---Hind---Express"))
        self.dropdown.setItemText(2, _translate("MainWindow", "1   2   5   1   3    Guwahati---SF---Express"))
        self.dropdown.setItemText(3, _translate("MainWindow", "1   2   5   0   8    Aronai---Express"))
        self.dropdown.setItemText(4, _translate("MainWindow", "1   5   7   0   8    Amrapali---Express"))
        self.dropdown.setItemText(5, _translate("MainWindow", "1   2   1   7   7    Mathura---Chambal---Express"))
        self.dropdown.setItemText(6, _translate("MainWindow", "1   2   3   8   1    Poorva---Express"))
        self.dropdown.setItemText(7, _translate("MainWindow", "2   2   8   1   7    Mysuru---Weekly---SF---Express"))
        self.dropdown.setItemText(8, _translate("MainWindow", "1   2   7   0   3    Falaknuma---Express"))
        self.dropdown.setItemText(9, _translate("MainWindow", "1   2   3   0   7    Jodhpur---Superfast---Express"))
        self.dropdown.setItemText(10, _translate("MainWindow", "1   5   7   2   2    Paharia---Express"))
        self.dropdown.setItemText(11, _translate("MainWindow", "1   2   8   6   0    Gitanjali---Express"))
        self.dropdown.setItemText(12, _translate("MainWindow", "1   2   3   2   7    Upasana---Express"))
        self.dropdown.setItemText(13, _translate("MainWindow", "1   3   0   0   9    Doon---Express"))
        self.dropdown.setItemText(14, _translate("MainWindow", "1   2   3   3   1    Himgiri---Express"))
        self.dropdown.setItemText(15, _translate("MainWindow", "1   8   6   2   7    Ranchi---Intercity---Express"))
        self.dropdown.setItemText(16, _translate("MainWindow", "1   2   5   0   7    Aronai---Express"))
        self.dropdown.setItemText(17, _translate("MainWindow", "1   2   3   0   5    New---Delhi---Rajdhani---Express"))
        self.dropdown.setItemText(18, _translate("MainWindow", "1   8   0   4   7    Amaravati---Express"))
        self.dropdown.setItemText(19, _translate("MainWindow", "1   8   6   4   5    East---Coast---Express"))
        self.dropdown.setItemText(20, _translate("MainWindow", "1   2   9   8   7    Ajmer---SF---Express"))
        self.dropdown.setItemText(21, _translate("MainWindow", "1   2   3   6   9    Kumbh---Express"))
        self.dropdown.setItemText(22, _translate("MainWindow", "1   3   0   0   5    Howrah---Amritsar---Mail"))
        self.dropdown.setItemText(23, _translate("MainWindow", "1   2   9   3   8    Garba---SF---Express"))
        self.dropdown.setItemText(24, _translate("MainWindow", "1   3   0   3   3    Howrah---Katihar---Express"))
        self.dropdown.setItemText(25, _translate("MainWindow", "1   2   3   1   5    Ananya---Express"))
        self.dropdown.setItemText(26, _translate("MainWindow", "1   2   3   2   9    West---Bengal---Sampark---Kranti---Express"))
        self.dropdown.setItemText(27, _translate("MainWindow", "5   8   0   0   1    Howrah---Puri---Passenger"))
        self.dropdown.setItemText(28, _translate("MainWindow", "0   0   1   1   4    Jaipur---One---Way---Special"))
        self.dropdown.setItemText(29, _translate("MainWindow", "2   2   9   1   2    Shirpa---Express"))
        self.dropdown.setItemText(30, _translate("MainWindow", "1   9   4   1   4    Sare---Jahan---Se---Acha---Express"))
        self.dropdown.setItemText(31, _translate("MainWindow", "1   2   8   7   1    Ispat---Express"))
        self.dropdown.setItemText(32, _translate("MainWindow", "1   2   0   2   3    Patna---Jan---Shatabdi---Express"))
        self.dropdown.setItemText(33, _translate("MainWindow", "2   0   8   8   9    Tirupati---Humsafar---Express"))
        self.dropdown.setItemText(34, _translate("MainWindow", "1   2   3   7   1    Bikaner---SF---Express"))
        self.dropdown.setItemText(35, _translate("MainWindow", "1   2   3   1   1    Kalka---Mail"))
        self.dropdown.setItemText(36, _translate("MainWindow", "1   2   6   6   5    Kanniyakumari---Superfast---Express"))
        self.dropdown.setItemText(37, _translate("MainWindow", "1   2   4   9   6    Pratap---Express"))
        self.dropdown.setItemText(38, _translate("MainWindow", "1   3   0   1   9    Bagh---Express"))
        self.dropdown.setItemText(39, _translate("MainWindow", "1   2   9   0   6    Porbandar---SF---Express"))
        self.dropdown.setItemText(40, _translate("MainWindow", "1   2   2   5   4    Anga---Express"))
        self.dropdown.setItemText(41, _translate("MainWindow", "2   2   5   0   2    KSR---Bengaluru---SF---Express"))
        self.dropdown.setItemText(42, _translate("MainWindow", "1   2   8   2   1     Dhauli---Express"))
        self.dropdown.setItemText(43, _translate("MainWindow", "2   0   8   2   2    Pune---Hamsafar---Express"))
        self.dropdown.setItemText(44, _translate("MainWindow", "1   2   2   6   2    Mumbai---CSMT---AC---Duronto---Express"))
        self.dropdown.setItemText(45, _translate("MainWindow", "1   3   0   0   7    Udyan---Abha---Toofan---Express"))
        self.dropdown.setItemText(46, _translate("MainWindow", "1   2   3   3   3    Vibhuti---Express"))
        self.dropdown.setItemText(47, _translate("MainWindow", "1   8   6   1   5    Kriya---Yoga---Express"))
        self.dropdown.setItemText(48, _translate("MainWindow", "1   2   3   1   7    Akal---Takht---Express"))
        self.dropdown.setItemText(49, _translate("MainWindow", "0   2   0   7   3    Jan---Shatabdi---Special"))
        self.tn.setText(_translate("MainWindow", "TRAIN NO"))
        self.tname.setText(_translate("MainWindow", "TRAIN NAME"))
        self.at.setText(_translate("MainWindow", "ARRIVAL TIME"))
        self.dt.setText(_translate("MainWindow", "DEPARTURE TIME"))
        self.pt.setText(_translate("MainWindow", "PLATFORM NO"))
        self.an.setText(_translate("MainWindow", "ANNOUNCEMENT"))
        self.details.setText(_translate("MainWindow", "CHECK STATUS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
