from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
led = Pin(2, Pin.OUT)

while True:
    input_state = button.value()
    led.value(input_state)

    print("Input:", input_state, "LED:", led.value())
    time.sleep(0.2)
