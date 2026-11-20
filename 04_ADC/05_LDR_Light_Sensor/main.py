from machine import ADC, Pin
import time

ldr = ADC(Pin(27))

while True:
    print("Light level:", ldr.read_u16())
    time.sleep(0.5)
