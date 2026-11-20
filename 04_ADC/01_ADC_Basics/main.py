from machine import ADC, Pin
import time

adc = ADC(Pin(26))

while True:
    value = adc.read_u16()
    print("ADC:", value)
    time.sleep(0.5)
