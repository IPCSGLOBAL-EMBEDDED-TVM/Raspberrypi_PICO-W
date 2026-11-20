from machine import Pin
import time

led = Pin(15, Pin.OUT)
last = time.ticks_ms()
interval = 500

while True:
    now = time.ticks_ms()
    if time.ticks_diff(now, last) >= interval:
        led.toggle()
        last = now
