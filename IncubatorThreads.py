import sys,os,os.path, time
from datetime import datetime,timedelta
from PyQt4 import QtCore, QtGui
from IncubatorPeripherals import Peripherals

class EggRollingThread(QtCore.QThread):
    signalRollingUpdate = QtCore.pyqtSignal(list)
    def __init__(self, myPeripheral):
        QtCore.QThread.__init__(self)
        self.myPeripheral = myPeripheral
    def __del__(self):
        self.quit()
        self.wait()
    def stop(self):
        self.terminate()
    def run(self):
        self.signalRollingUpdate.emit(["Egg Rolling in Progress",3000])
        self.myPeripheral.set_servo(1)
        self.myPeripheral.forward()
        self.sleep(1)
        self.signalRollingUpdate.emit(["Egg Rolling in Progress", 3000])
        self.myPeripheral.backward()
        self.sleep(1)
        self.signalRollingUpdate.emit(["Egg Rolling in Progress", 3000])
        self.myPeripheral.forward()
        self.sleep(1)
        self.signalRollingUpdate.emit(["Egg Rolling in Progress", 3000])
        self.myPeripheral.backward()
        self.myPeripheral.set_servo(0)
        self.signalRollingUpdate.emit(["Egg Rolling Finished",3000])

class PreheatThread(QtCore.QThread):
    signalPreHeatDone = QtCore.pyqtSignal()
    signalUpdate = QtCore.pyqtSignal(dict)
    def __init__(self, myPeripheral):
        QtCore.QThread.__init__(self)
        self.myPeripheral = myPeripheral
    def __del__(self):
        self.quit()
        self.wait()
    def stop(self):
        self.terminate()
    def get_current_values(self):
        current_values = {}
        self.myPeripheral.read_sensor()
        current_values["T"] = self.myPeripheral.get_temp()
        current_values["H"] = self.myPeripheral.get_hum()
        current_values["F"] = self.myPeripheral.get_fan_status()
        current_values["S"] = self.myPeripheral.get_heat_status()
        return current_values
    def run(self):
        self.myPeripheral.read_sensor()
        while self.myPeripheral.get_temp()<99.5: #99.5
            if self.myPeripheral.get_heat_status()!=1:
                self.myPeripheral.set_heat(1)
                self.myPeripheral.set_fan(1)
            self.signalUpdate.emit(self.get_current_values())
            self.msleep(500)
            if self.get_current_values()["T"]>=99.5:
                self.msleep(200)
                self.signalUpdate.emit(self.get_current_values())
        self.myPeripheral.set_heat(0)
        self.myPeripheral.set_fan(1)
        self.signalUpdate.emit(self.get_current_values())
        self.sleep(5)
        self.myPeripheral.set_fan(0)
        self.signalUpdate.emit(self.get_current_values())
        self.signalPreHeatDone.emit()

class IncubationProcessThread(QtCore.QThread):
    signalIncubationDone = QtCore.pyqtSignal()
    signalUpdate = QtCore.pyqtSignal(dict)
    signalStatusBarUpdate = QtCore.pyqtSignal(list)
    signalMainTextUpdate = QtCore.pyqtSignal(list)
    def __init__(self, myPeripheral):
        QtCore.QThread.__init__(self)
        self.myPeripheral = myPeripheral
        self.EggRolling = EggRollingThread(self.myPeripheral)
        self.lowerTemp = 98.5
        self.upperTemp = 100.5
    def __del__(self):
        self.quit()
        self.wait()
    def stop(self):
        self.EggRolling.stop()
        self.terminate()
    def days_hours_minutes(self, td):
        return [ td.days, td.seconds // 3600, (td.seconds // 60) % 60 ]
    def get_current_values(self):
        current_values = {}
        self.myPeripheral.read_sensor()
        current_values["T"] = self.myPeripheral.get_temp()
        current_values["H"] = self.myPeripheral.get_hum()
        current_values["F"] = self.myPeripheral.get_fan_status()
        current_values["S"] = self.myPeripheral.get_heat_status()
        current_values["T2G"] = self.days_hours_minutes(self.endDate - datetime.now())
        return current_values
    def run(self):
        self.startDate = datetime.now()
        self.endDate = self.startDate + timedelta(days=21)
        self.cycleCounter = 0
        self.lastTimeFanOn = self.startDate
        self.lastTimeMotorOn = self.startDate
        while self.days_hours_minutes(self.endDate - datetime.now())[0] > 0:
            self.signalUpdate.emit(self.get_current_values())
            if (datetime.now() - self.startDate).days >=7:
                if datetime.now().hour>=2 and datetime.now().hour<4:
                    self.lowerTemp = 70.0
                    self.upperTemp = 75.0
                    self.signalMainTextUpdate.emit(["Incubation In Progress...",
                                                    "Incubation In Progress...\nDaily Cool Down Cycle Active"])
                else:
                    self.lowerTemp = 98.5
                    self.upperTemp = 100.5
                    self.signalMainTextUpdate.emit(["Incubation In Progress...\nDaily Cool Down Cycle Active",
                                                    "Incubation In Progress..."])
            if self.myPeripheral.get_temp() < self.lowerTemp:
                self.myPeripheral.set_heat(1)
                self.myPeripheral.set_fan(1)
                self.lastTimeFanOn = datetime.now()
            elif self.myPeripheral.get_temp() > self.upperTemp:
                self.myPeripheral.set_heat(0)
                self.myPeripheral.set_fan(1)
                self.lastTimeFanOn = datetime.now()
            else:
                if self.days_hours_minutes(datetime.now() - self.lastTimeFanOn)[2] >= 15: #Number of Min. to wait before On the Fan
                    self.myPeripheral.set_fan(1)
                    self.cycleCounter += 1
                    self.lastTimeFanOn = datetime.now()
                elif self.cycleCounter > 0 and self.cycleCounter < 21: #Number of Sec. while the Fan On (2 Cycle/Sec * 10 Sec = 20)
                    self.cycleCounter += 1
                else:
                    self.cycleCounter = 0
                    self.myPeripheral.set_heat(0)
                    self.myPeripheral.set_fan(0)
            self.signalUpdate.emit(self.get_current_values())
            if self.myPeripheral.get_hum() < 40.0:
                self.signalStatusBarUpdate.emit(["Wet Sponges to Raise Humidity",2000])
            elif self.myPeripheral.get_hum() > 60.0:
                self.signalStatusBarUpdate.emit(["Humidity is Very High", 2000])
            if self.days_hours_minutes(datetime.now() - self.lastTimeMotorOn)[1] >= 5: #Number of hours to wait before Rolling Eggs
                self.lastTimeMotorOn = datetime.now()
                self.EggRolling.start()
            self.msleep(500) #2 Cycle/Sec
            self.signalUpdate.emit(self.get_current_values())

class IncubationThread(QtCore.QThread):
    signalStart = QtCore.pyqtSignal()
    signalRefuseStart = QtCore.pyqtSignal()
    signalSetTime = QtCore.pyqtSignal()
    signalPreHeatStart = QtCore.pyqtSignal()
    signalPreHeatDone = QtCore.pyqtSignal(int)
    signalAskforCancel = QtCore.pyqtSignal()
    signalUpdate = QtCore.pyqtSignal(dict)
    signalStartIncubation = QtCore.pyqtSignal()
    signalFirst = QtCore.pyqtSignal()
    signalSecond = QtCore.pyqtSignal()
    signalThird = QtCore.pyqtSignal()
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.myPeripheral = Peripherals()
        self.preheat_thread = PreheatThread(self.myPeripheral)
        self.incubation_thread = IncubationProcessThread(self.myPeripheral)
    def __del__(self):
        self.quit()
        self.wait()
    def stop(self):
        self.preheat_thread.stop()
        self.incubation_thread.stop()
        self.myPeripheral.clean_pins()
        #self.myPeripheral.pi.stop()
        self.terminate()
    def wait_signal(self, signal_1, signal_2=None, signal_3=None, timeout=None):
        loop = QtCore.QEventLoop()
        signal_1.connect(lambda: loop.exit(1))
        if signal_2 != None:
            signal_2.connect(lambda: loop.exit(2))
        if signal_3 != None:
            signal_3.connect(lambda: loop.exit(3))
        if timeout != None:
            QtCore.QTimer.singleShot(timeout, lambda: loop.exit(-1))
        return loop.exec_()
    def run(self):
        #Ask For start Incubation Cycle
        return_value = self.wait_signal(self.signalFirst, self.signalSecond, None, None)
        if return_value == 1:
            self.signalSetTime.emit()
            self.wait_signal(self.signalThird, None, None, None)
            self.signalPreHeatStart.emit()
            #Start Preheat
            self.preheat_thread.start()
            #Wait for Preheat Done or Canceled
            return_value = self.wait_signal(self.preheat_thread.signalPreHeatDone, self.signalThird, None, None)
            while return_value != 1:
                self.signalAskforCancel.emit()
                return_value = self.wait_signal(self.signalFirst, self.signalSecond, None, None)
                if return_value == 2: #If user Refuse the Cancel
                    self.signalPreHeatStart.emit()
                    return_value = self.wait_signal(self.preheat_thread.signalPreHeatDone, self.signalThird, None, None)
                elif return_value == 1: #If user Accept the Cancel
                    self.preheat_thread.terminate()
                    self.signalRefuseStart.emit()
                    return
            #Ask for Set Eggs
            return_value = self.wait_signal(self.signalFirst, self.signalThird, None, None)
            while return_value != 1:
                self.signalAskforCancel.emit()
                return_value = self.wait_signal(self.signalFirst, self.signalSecond, None, None)
                if return_value == 2: #If user Refuse the Cancel
                    self.preheat_thread.signalPreHeatDone.emit()
                    self.msleep(100)
                    return_value = self.wait_signal(self.signalFirst, self.signalThird, None, None)
                elif return_value == 1: #If user Accept the Cancel
                    self.signalRefuseStart.emit()
                    return
            #If Set Eggs is Completed
            self.signalStartIncubation.emit()
            self.incubation_thread.start()
            return_value = self.wait_signal(self.incubation_thread.signalIncubationDone, self.signalThird, None, None)
            while return_value != 1:
                self.signalAskforCancel.emit()
                return_value = self.wait_signal(self.signalFirst, self.signalSecond, None, None)
                if return_value == 2:  # If user Refuse the Cancel
                    self.signalStartIncubation.emit()
                    self.msleep(100)
                    return_value = self.wait_signal(self.incubation_thread.signalIncubationDone, self.signalThird, None, None)
                elif return_value == 1:  # If user Accept the Cancel
                    self.signalRefuseStart.emit()
                    return
        elif return_value == 2:
            self.signalRefuseStart.emit()

class WelcomeThread(QtCore.QThread):
    signalInit = QtCore.pyqtSignal()
    def __init__(self):
        QtCore.QThread.__init__(self)
    def __del__(self):
        self.quit()
        self.wait()
    def run(self):
        self.sleep(2)
        self.signalInit.emit()