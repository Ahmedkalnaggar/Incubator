import pigpio,time

class Peripherals:
    def __init__(self):
        self.servo_status = 1
        self.SERVO_POWER_PIN = 26
        self.SERVO_CONTROLE_PIN = 13
        self.SERVO_MAX_VALUE = 2000 #Must be a Number between 1000 and 2000
        self.pi = pigpio.pi()
        self.setup_pins()
        self.clean_pins()
    def get_servo_status(self):
        return self.servo_status
    def set_servo(self, status=0):
        if self.servo_status != status:
            self.servo_status = status
            self.pi.write(self.SERVO_POWER_PIN, not status)
    def setup_pins(self):
        self.pi.set_mode(self.SERVO_POWER_PIN, pigpio.OUTPUT)
        self.pi.set_mode(self.SERVO_CONTROLE_PIN, pigpio.ALT0)
        self.pi.set_PWM_frequency(self.SERVO_CONTROLE_PIN, 50)
        self.pi.set_PWM_range(self.SERVO_CONTROLE_PIN, 20000)
    def clean_pins(self):
        self.set_servo(0)
    def forward(self):
        for i in range(1000, self.SERVO_MAX_VALUE+1, 1):
            self.pi.set_PWM_dutycycle(self.SERVO_CONTROLE_PIN, i)
            time.sleep(0.01)
    def backward(self):
        for i in range(self.SERVO_MAX_VALUE, 999, -1):
            self.pi.set_PWM_dutycycle(self.SERVO_CONTROLE_PIN, i)
            time.sleep(0.01)

myPeripheral = Peripherals()
myPeripheral.set_servo(1)
print("Egg Rolling Forward")
myPeripheral.forward()
time.sleep(1)
print("Egg Rolling Backward")
myPeripheral.backward()
myPeripheral.set_servo(0)
myPeripheral.pi.stop()