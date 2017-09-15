import DHT22
import pigpio,time

class Peripherals:
    def __init__(self):
        self.heat_status = 1
        self.fan_status = 1
        self.servo_status = 1
        self.DHT_PIN = 6
        self.FAN_PIN = 12
        self.HEAT_PIN = 16
        self.SERVO_POWER_PIN = 26
        self.SERVO_CONTROLE_PIN = 13
        self.pi = pigpio.pi()
        self.DHT_Sensor = DHT22.sensor(self.pi, self.DHT_PIN, LED=None, power=None)
        self.setup_pins()
        self.clean_pins()
        self.read_sensor()
    def read_sensor(self):
        self.DHT_Sensor.trigger()
        time.sleep(0.2)
        self.temp = self.round_temp(self.DHT_Sensor.temperature())
        self.humidity = self.round_hum(self.DHT_Sensor.humidity())
    def get_temp(self):
        return self.temp
    def round_temp(self, inputTemp):
        return round((inputTemp * 9 / 5 + 32) * 1.00, 1)  # Convert to F and Factor
    def get_hum(self):
        return self.humidity
    def round_hum(self, inputHum):
        return round(inputHum * 1.00, 1)  # Factor
    def get_heat_status(self):
        return self.heat_status
    def get_fan_status(self):
        return self.fan_status
    def get_servo_status(self):
        return self.servo_status
    def set_heat(self, status = 0):
        if self.heat_status != status:
            self.heat_status = status
            self.pi.write(self.HEAT_PIN, not status)
    def set_fan(self, status = 0):
        if self.fan_status != status:
            self.fan_status = status
            self.pi.write(self.FAN_PIN, not status)
    def set_servo(self, status=0):
        if self.servo_status != status:
            self.servo_status = status
            self.pi.write(self.SERVO_POWER_PIN, not status)
    def setup_pins(self):
        self.pi.set_mode(self.HEAT_PIN, pigpio.OUTPUT)
        self.pi.set_mode(self.FAN_PIN, pigpio.OUTPUT)
        self.pi.set_mode(self.SERVO_POWER_PIN, pigpio.OUTPUT)
        self.pi.set_mode(self.SERVO_CONTROLE_PIN, pigpio.ALT0)
        self.pi.set_PWM_frequency(self.SERVO_CONTROLE_PIN, 50)
        self.pi.set_PWM_range(self.SERVO_CONTROLE_PIN, 20000)
    def clean_pins(self):
        self.set_servo(0)
        self.set_fan(0)
        self.set_heat(0)
    def forward(self):
        for i in range(1000, 2001, 1):
            self.pi.set_PWM_dutycycle(self.SERVO_CONTROLE_PIN, i)
            time.sleep(0.01)
    def backward(self):
        for i in range(2000, 999, -1):
            self.pi.set_PWM_dutycycle(self.SERVO_CONTROLE_PIN, i)
            time.sleep(0.01)
