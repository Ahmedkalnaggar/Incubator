import sys,os,os.path, time
from datetime import datetime,timedelta
from PyQt4 import QtCore, QtGui
from IncubatorPeripherals import Peripherals

class TimerThread(QtCore.QThread):
    signalTimerDone = QtCore.pyqtSignal()
    def __init__(self, delta = [0,0]):
        QtCore.QThread.__init__(self)
        self.startTime = None
        self.endTime = None
        self.deltaTime = delta
    def __del__(self):
        self.quit()
        self.wait()
    def stop(self):
        self.terminate()
    def hours_minutes(self, td):
        return [ td.seconds // 3600, (td.seconds // 60) % 60 ]
    def run(self):
        self.startTime = datetime.now()
        self.endTime = self.startTime + timedelta(hours=self.deltaTime[0],minutes=self.deltaTime[1])
        self.currentDifference = self.hours_minutes(self.endTime - datetime.now())
        while self.currentDifference[0] > 0 or self.currentDifference[1] > 0 :
            time.sleep(1)
            self.currentDifference = self.hours_minutes(self.endTime - datetime.now())
        self.signalTimerDone.emit()

class EggRollingThread(QtCore.QThread):
    signalRollingStarted = QtCore.pyqtSignal(list)
    signalRollingFinished = QtCore.pyqtSignal(list)
    def __init__(self, myPeripheral):
        QtCore.QThread.__init__(self)
        self.myPeripheral = myPeripheral
    def __del__(self):
        self.quit()
        self.wait()
    def stop(self):
        self.terminate()
    def run(self):
        self.signalRollingStarted.emit(["Egg Rolling in Progress",0])
        self.myPeripheral.set_servo(1)
        self.myPeripheral.forward()
        time.sleep(1)
        self.myPeripheral.backward()
        time.sleep(1)
        self.myPeripheral.forward()
        time.sleep(1)
        self.myPeripheral.backward()
        self.myPeripheral.set_servo(0)
        self.signalRollingFinished.emit(["Egg Rolling Finished",3000])

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
        while self.myPeripheral.get_temp()<85.5: #99.5
            if self.myPeripheral.get_heat_status()!=1:
                self.myPeripheral.set_heat(1)
                self.myPeripheral.set_fan(1)
            self.signalUpdate.emit(self.get_current_values())
            time.sleep(1)
        self.myPeripheral.set_heat(0)
        self.myPeripheral.set_fan(1)
        self.signalUpdate.emit(self.get_current_values())
        time.sleep(5)
        self.myPeripheral.set_fan(0)
        self.signalUpdate.emit(self.get_current_values())
        self.signalPreHeatDone.emit()

class IncubationProcessThread(QtCore.QThread):
    signalIncubationDone = QtCore.pyqtSignal()
    signalUpdate = QtCore.pyqtSignal(dict)
    def __init__(self, myPeripheral):
        QtCore.QThread.__init__(self)
        self.myPeripheral = myPeripheral
        self.EggRolling = EggRollingThread(self.myPeripheral)
        self.startDate = datetime.now()
        self.endDate = self.startDate + timedelta(days=21)
        self.cycleCounter = 0
        self.lastTimeFanOn = datetime.now()
        self.lastTimeMotorOn = datetime.now()
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
        while self.days_hours_minutes(self.endDate - datetime.now())[0] > 0:
            self.signalUpdate.emit(self.get_current_values())
            if self.myPeripheral.get_temp() < 84.5: #98.5
                self.myPeripheral.set_heat(1)
                self.myPeripheral.set_fan(1)
                self.lastTimeFanOn = datetime.now()
            elif self.myPeripheral.get_temp() > 86.5: #100.5
                self.myPeripheral.set_heat(0)
                self.myPeripheral.set_fan(1)
                self.lastTimeFanOn = datetime.now()
            else:
                if self.days_hours_minutes(datetime.now() - self.lastTimeFanOn)[2] >= 15: #Number of Min. to wait before On the Fan
                    self.myPeripheral.set_fan(1)
                    self.cycleCounter += 1
                    self.lastTimeFanOn = datetime.now()
                elif self.cycleCounter > 0 and self.cycleCounter < 11: #Number of Sec. while the Fan On
                    self.cycleCounter += 1
                else:
                    self.cycleCounter = 0
                    self.myPeripheral.set_heat(0)
                    self.myPeripheral.set_fan(0)
            self.signalUpdate.emit(self.get_current_values())
            if self.days_hours_minutes(datetime.now() - self.lastTimeMotorOn)[1] >= 5: #Number of hours to wait before Rolling Eggs
                self.lastTimeMotorOn = datetime.now()
                self.EggRolling.start()
            time.sleep(1)

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
        self.myPeripheral.pi.stop()
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
                    time.sleep(0.1)
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
                    time.sleep(0.1)
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
        time.sleep(2)
        self.signalInit.emit()