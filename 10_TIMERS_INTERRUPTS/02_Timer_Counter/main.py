from machine import Timer
import time

count = 0

def callback(timer):
    global count
    count += 1

timer = Timer()
timer.init(period=1000, mode=Timer.PERIODIC, callback=callback)

while True:
    print("Timer events:", count)
    time.sleep(2)
