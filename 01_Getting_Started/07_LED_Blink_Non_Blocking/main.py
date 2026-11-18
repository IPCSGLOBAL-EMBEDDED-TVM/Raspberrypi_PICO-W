from machine import Pin
import time

led = Pin(15, Pin.OUT)
previous_time = time.ticks_ms()
state = 0

while True:
    current_time = time.ticks_ms()

    if time.ticks_diff(current_time, previous_time) >= 500:
        state = not state
        led.value(state)
        previous_time = current_time
