from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

interrupt_flag = False

def button_callback(pin):
    global interrupt_flag
    interrupt_flag = True

button.irq(trigger=Pin.IRQ_FALLING, handler=button_callback)

last_press = time.ticks_ms()

while True:
    if interrupt_flag:
        interrupt_flag = False
        now = time.ticks_ms()

        if time.ticks_diff(now, last_press) > 200:
            led.toggle()
            print("GPIO interrupt detected")
            last_press = now

    time.sleep_ms(10)
