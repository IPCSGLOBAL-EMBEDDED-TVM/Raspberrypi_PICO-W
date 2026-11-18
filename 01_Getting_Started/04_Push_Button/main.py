from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        print("Button Pressed")
    else:
        print("Button Released")

    time.sleep(0.2)
