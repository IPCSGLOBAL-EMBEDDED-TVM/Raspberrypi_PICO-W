from machine import ADC
import time

sensor = ADC(4)

while True:
    voltage = sensor.read_u16() * 3.3 / 65535
    temperature = 27 - (voltage - 0.706) / 0.001721
    print("Approx. chip temperature:", round(temperature, 2), "C")
    time.sleep(2)
