from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    print("Button state:", button.value())
    time.sleep(0.2)
