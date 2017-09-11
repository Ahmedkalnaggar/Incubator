import sys,os,os.path,datetime, time
from PyQt4 import QtCore, QtGui
from IncubatorGUI import Ui_MainWindow
from IncubatorThreads import WelcomeThread,IncubationThread

class Incubator(Ui_MainWindow):
    def __init__(self, dialog):
        super(Incubator, self).__init__()
        self.setupUi(dialog)
        self.pushButton_1.clicked.connect(self.first_button_clicked)
        self.pushButton_2.clicked.connect(self.second_button_clicked)
        self.pushButton_3.clicked.connect(self.third_button_clicked)
        self.welcome_thread = WelcomeThread()
        self.welcome_thread.signalInit.connect(self.hide_start_screen)
        self.main_thread = IncubationThread()
        self.main_thread.signalSetTime.connect(self.set_time)
        self.main_thread.signalPreHeatStart.connect(self.preheat_start)
        self.main_thread.signalAskforCancel.connect(self.ask_cancel)
        self.main_thread.preheat_thread.signalUpdate.connect(self.update_bar)
        self.main_thread.preheat_thread.signalPreHeatDone.connect(self.preheat_finished)
        self.main_thread.signalRefuseStart.connect(self.show_start_screen)
        self.main_thread.signalStartIncubation.connect(self.incubation_progress)
        self.main_thread.incubation_thread.signalUpdate.connect(self.update_bar)
        self.main_thread.incubation_thread.EggRolling.signalRollingStarted.connect(self.update_statusbar)
        self.main_thread.incubation_thread.EggRolling.signalRollingFinished.connect(self.update_statusbar)
        self.welcome_thread.start()

    def show_start_screen(self):
        self.widget_1.hide()
        self.widget_6.show()
        self.maintext_2.setText("Powering off, To turn back on, remove power and re-apply power")
        self.main_thread.stop()
        self.statusbar.clearMessage()

    def hide_start_screen(self):
        self.widget_6.hide()
        self.ask_for_start()

    def ask_for_start(self):
        self.maintext.setText("Start Incubation Cycle?")
        self.pushButton_1.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(False)
        self.main_thread.start()

    def ask_cancel(self):
        self.maintext.setText("Cancel Cycle ?")
        self.pushButton_1.setText("Yes")
        self.pushButton_2.setText("No")
        self.pushButton_1.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(False)

    def update_bar(self, values):
        self.T_label.setText("T: {} F".format(str(values["T"])))
        self.H_label.setText("| H: {}% RH".format(str(values["H"])))
        if values["F"]==1:
            self.textBrowser_2.setStyleSheet("background-color:red")
        else:
            self.textBrowser_2.setStyleSheet("background-color:white")
        if values["S"]==1:
            self.textBrowser_1.setStyleSheet("background-color:red")
        else:
            self.textBrowser_1.setStyleSheet("background-color:white")
        if values.has_key("T2G"):
            self.D_label.setText("| T2G: {}D {}H {}M".format(values["T2G"][0],values["T2G"][1],values["T2G"][2]))

    def update_statusbar(self, values):
        self.statusbar.clearMessage()
        self.statusbar.showMessage(values[0], values[1])

    def preheat_start(self):
        print(self.dateTimeEdit.dateTime().toPyDateTime())
        self.widget_5.hide()
        self.maintext.setText("Preheating Incubator, Please Wait to Set Eggs")
        self.widget_1.show()
        self.pushButton_1.setText("Yes")
        self.pushButton_1.setEnabled(False)
        self.pushButton_2.setText("No")
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setText("Cancel")
        self.pushButton_3.setEnabled(True)

    def preheat_finished(self):
        self.maintext.setText("Ready to Set Eggs Press Continue when lid is back on")
        self.pushButton_1.setText("Continue")
        self.pushButton_1.setEnabled(True)
        self.pushButton_2.setText("No")
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setText("Cancel")
        self.pushButton_3.setEnabled(True)

    def incubation_progress(self):
        self.maintext.setText("Incubation In Progress...")
        self.pushButton_1.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(True)
        self.return_normal_buttons()

    def set_time(self):
        self.pushButton_1.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.widget_5.show()
        self.maintext.setText("Set Current Time\n\n")
        self.pushButton_1.setText("+")
        self.pushButton_2.setText("-")
        self.pushButton_3.setText("Done")
        self.pushButton_1.clicked.connect(lambda: self.dateTimeEdit.stepUp())
        self.pushButton_2.clicked.connect(lambda: self.dateTimeEdit.stepDown())
        self.pushButton_3.clicked.connect(self.return_normal_buttons)

    def return_normal_buttons(self):
        self.pushButton_1.clicked.connect(self.first_button_clicked)
        self.pushButton_2.clicked.connect(self.second_button_clicked)
        self.pushButton_3.clicked.connect(self.third_button_clicked)

    def first_button_clicked(self):
        self.main_thread.signalFirst.emit()

    def second_button_clicked(self):
        self.main_thread.signalSecond.emit()

    def third_button_clicked(self):
        self.main_thread.signalThird.emit()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    prog = Incubator(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())