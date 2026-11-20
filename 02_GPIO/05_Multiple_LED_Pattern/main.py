from machine import Pin
import time

leds = [
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT)
]

while True:
    for led in leds:
        led.on()
        time.sleep(0.3)
        led.off()

    for led in reversed(leds):
        led.on()
        time.sleep(0.3)
        led.off()
