from machine import ADC, Pin
import time

sensor = ADC(Pin(28))

while True:
    raw = sensor.read_u16()
    voltage = raw * 3.3 / 65535
    print("Sensor:", raw, "Voltage:", round(voltage, 3))
    time.sleep(0.5)
