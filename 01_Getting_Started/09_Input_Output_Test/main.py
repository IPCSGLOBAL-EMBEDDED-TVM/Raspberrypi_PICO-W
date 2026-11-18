from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)

while True:
    state = button.value()
    led.value(state)

    print("Input:", state, "Output:", led.value())
    time.sleep(0.5)
