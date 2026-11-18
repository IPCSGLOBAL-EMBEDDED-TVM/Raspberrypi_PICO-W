from machine import Pin
import time

led1 = Pin(14, Pin.OUT)
led2 = Pin(15, Pin.OUT)
led3 = Pin(16, Pin.OUT)

while True:
    for led in (led1, led2, led3):
        led.on()
        time.sleep(0.5)
        led.off()
