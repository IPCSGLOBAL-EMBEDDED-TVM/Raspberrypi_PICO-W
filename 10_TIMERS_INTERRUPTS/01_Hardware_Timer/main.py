from machine import Pin, Timer
import time

led = Pin(15, Pin.OUT)

def timer_callback(timer):
    led.toggle()

timer = Timer()
timer.init(period=500, mode=Timer.PERIODIC, callback=timer_callback)

while True:
    time.sleep(1)
