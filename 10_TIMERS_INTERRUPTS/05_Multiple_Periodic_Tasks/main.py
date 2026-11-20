from machine import Pin
import time

led1 = Pin(15, Pin.OUT)
led2 = Pin(16, Pin.OUT)

last1 = time.ticks_ms()
last2 = time.ticks_ms()

while True:
    now = time.ticks_ms()

    if time.ticks_diff(now, last1) >= 500:
        led1.toggle()
        last1 = now

    if time.ticks_diff(now, last2) >= 1000:
        led2.toggle()
        last2 = now
