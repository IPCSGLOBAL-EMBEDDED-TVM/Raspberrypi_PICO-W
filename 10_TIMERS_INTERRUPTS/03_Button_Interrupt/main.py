from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)
event = False

def irq_handler(pin):
    global event
    event = True

button.irq(trigger=Pin.IRQ_FALLING, handler=irq_handler)

while True:
    if event:
        event = False
        led.toggle()
        time.sleep_ms(200)
    time.sleep_ms(10)
