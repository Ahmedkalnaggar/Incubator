# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewIncubatorGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 320)
        MainWindow.setMinimumSize(QtCore.QSize(480, 320))
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget_1 = QtGui.QWidget(self.centralwidget)
        self.widget_1.setEnabled(True)
        self.widget_1.setGeometry(QtCore.QRect(10, 10, 461, 31))
        self.widget_1.setObjectName(_fromUtf8("widget_1"))
        self.T_label = QtGui.QLabel(self.widget_1)
        self.T_label.setGeometry(QtCore.QRect(0, 0, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.T_label.setFont(font)
        self.T_label.setObjectName(_fromUtf8("T_label"))
        self.F_label = QtGui.QLabel(self.widget_1)
        self.F_label.setGeometry(QtCore.QRect(330, 0, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.F_label.setFont(font)
        self.F_label.setObjectName(_fromUtf8("F_label"))
        self.S_label = QtGui.QLabel(self.widget_1)
        self.S_label.setGeometry(QtCore.QRect(390, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.S_label.setFont(font)
        self.S_label.setObjectName(_fromUtf8("S_label"))
        self.H_label = QtGui.QLabel(self.widget_1)
        self.H_label.setGeometry(QtCore.QRect(70, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.H_label.setFont(font)
        self.H_label.setObjectName(_fromUtf8("H_label"))
        self.D_label = QtGui.QLabel(self.widget_1)
        self.D_label.setGeometry(QtCore.QRect(170, 0, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.D_label.setFont(font)
        self.D_label.setObjectName(_fromUtf8("D_label"))
        self.textBrowser_1 = QtGui.QTextBrowser(self.widget_1)
        self.textBrowser_1.setGeometry(QtCore.QRect(430, 5, 21, 21))
        self.textBrowser_1.setAcceptDrops(True)
        self.textBrowser_1.setFrameShape(QtGui.QFrame.Box)
        self.textBrowser_1.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_1.setTabChangesFocus(False)
        self.textBrowser_1.setOpenLinks(False)
        self.textBrowser_1.setObjectName(_fromUtf8("textBrowser_1"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.widget_1)
        self.textBrowser_2.setGeometry(QtCore.QRect(360, 5, 21, 21))
        self.textBrowser_2.setAcceptDrops(True)
        self.textBrowser_2.setFrameShape(QtGui.QFrame.Box)
        self.textBrowser_2.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setTabChangesFocus(False)
        self.textBrowser_2.setOpenLinks(False)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 60, 261, 161))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.maintext = QtGui.QLabel(self.widget_2)
        self.maintext.setGeometry(QtCore.QRect(0, 0, 261, 161))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.maintext.setFont(font)
        self.maintext.setTextFormat(QtCore.Qt.AutoText)
        self.maintext.setScaledContents(False)
        self.maintext.setAlignment(QtCore.Qt.AlignCenter)
        self.maintext.setWordWrap(True)
        self.maintext.setObjectName(_fromUtf8("maintext"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.widget_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 0, 261, 161))
        self.textBrowser_3.setAcceptDrops(True)
        self.textBrowser_3.setFrameShape(QtGui.QFrame.Box)
        self.textBrowser_3.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setTabChangesFocus(False)
        self.textBrowser_3.setOpenLinks(False)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.widget_5 = QtGui.QWidget(self.widget_2)
        self.widget_5.setGeometry(QtCore.QRect(0, 80, 261, 81))
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.widget_5)
        self.dateTimeEdit.setGeometry(QtCore.QRect(0, 0, 261, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTimeEdit.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2025, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateTimeEdit.setMinimumDate(QtCore.QDate(2017, 1, 1))
        self.dateTimeEdit.setCalendarPopup(False)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.textBrowser_3.raise_()
        self.maintext.raise_()
        self.widget_5.raise_()
        self.widget_5.raise_()
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(279, 60, 191, 161))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.pushButton_1 = QtGui.QPushButton(self.widget_3)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 10, 171, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_2 = QtGui.QPushButton(self.widget_3)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 60, 171, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.widget_3)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 110, 171, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.widget_4 = QtGui.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(10, 240, 461, 51))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.logo = QtGui.QLabel(self.widget_4)
        self.logo.setGeometry(QtCore.QRect(340, 0, 121, 51))
        self.logo.setText(_fromUtf8(""))
        self.logo.setTextFormat(QtCore.Qt.AutoText)
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8("Logo25.png")))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.label2_downbar = QtGui.QLabel(self.widget_4)
        self.label2_downbar.setGeometry(QtCore.QRect(100, 20, 231, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label2_downbar.setFont(font)
        self.label2_downbar.setObjectName(_fromUtf8("label2_downbar"))
        self.label_downbar = QtGui.QLabel(self.widget_4)
        self.label_downbar.setGeometry(QtCore.QRect(10, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_downbar.setFont(font)
        self.label_downbar.setObjectName(_fromUtf8("label_downbar"))
        self.widget_6 = QtGui.QWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(10, 60, 461, 161))
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.textBrowser_5 = QtGui.QTextBrowser(self.widget_6)
        self.textBrowser_5.setGeometry(QtCore.QRect(0, 0, 461, 161))
        self.textBrowser_5.setAcceptDrops(True)
        self.textBrowser_5.setFrameShape(QtGui.QFrame.Box)
        self.textBrowser_5.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setTabChangesFocus(False)
        self.textBrowser_5.setOpenLinks(False)
        self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        self.maintext_2 = QtGui.QLabel(self.widget_6)
        self.maintext_2.setGeometry(QtCore.QRect(0, 0, 461, 161))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.maintext_2.setFont(font)
        self.maintext_2.setTextFormat(QtCore.Qt.AutoText)
        self.maintext_2.setScaledContents(False)
        self.maintext_2.setAlignment(QtCore.Qt.AlignCenter)
        self.maintext_2.setWordWrap(True)
        self.maintext_2.setObjectName(_fromUtf8("maintext_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.widget_1.hide()
        self.widget_5.hide()
        #MainWindow.showFullScreen()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Incubator Model 32", None))
        self.T_label.setText(_translate("MainWindow", "T: 85.5 F", None))
        self.F_label.setText(_translate("MainWindow", "Fan:", None))
        self.S_label.setText(_translate("MainWindow", "Heat:", None))
        self.H_label.setText(_translate("MainWindow", "| H: 38.6% RH", None))
        self.D_label.setText(_translate("MainWindow", "| T2G: 21D 00H 00M", None))
        self.maintext.setText(_translate("MainWindow", "Start Incubation Cycle?", None))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "M/d/yyyy h:mm AP", None))
        self.pushButton_1.setText(_translate("MainWindow", "Yes", None))
        self.pushButton_2.setText(_translate("MainWindow", "No", None))
        self.pushButton_3.setText(_translate("MainWindow", "Cancel", None))
        self.label2_downbar.setText(_translate("MainWindow", " Model 32 | Software Version 1.0", None))
        self.label_downbar.setText(_translate("MainWindow", "Incubator", None))
        self.maintext_2.setText(_translate("MainWindow", "Incubator Process Loading… Please Wait", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())