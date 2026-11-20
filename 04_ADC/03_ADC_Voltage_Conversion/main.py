from machine import ADC, Pin
import time

adc = ADC(Pin(26))
VREF = 3.3

while True:
    raw = adc.read_u16()
    voltage = raw * VREF / 65535
    print("Raw:", raw, "Voltage:", round(voltage, 3), "V")
    time.sleep(0.5)
