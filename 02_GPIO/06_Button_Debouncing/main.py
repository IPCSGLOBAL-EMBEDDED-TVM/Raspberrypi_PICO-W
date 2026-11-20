from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
led = Pin(2, Pin.OUT)

last_state = 0
stable_state = 0
last_change = time.ticks_ms()
debounce_ms = 50

while True:
    current_state = button.value()

    if current_state != last_state:
        last_change = time.ticks_ms()
        last_state = current_state

    if time.ticks_diff(time.ticks_ms(), last_change) >= debounce_ms:
        if current_state != stable_state:
            stable_state = current_state
            if stable_state:
                led.toggle()
                print("Valid button press")

    time.sleep_ms(5)
