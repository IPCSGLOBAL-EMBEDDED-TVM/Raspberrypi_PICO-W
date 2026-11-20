from machine import ADC, Pin
import time

pot = ADC(Pin(26))

while True:
    print("Potentiometer:", pot.read_u16())
    time.sleep(0.2)
