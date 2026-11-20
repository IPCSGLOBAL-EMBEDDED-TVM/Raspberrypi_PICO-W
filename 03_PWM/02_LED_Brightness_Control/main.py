from machine import Pin, PWM
import time

led = PWM(Pin(15))
led.freq(1000)

while True:
    led.duty_u16(10000)
    time.sleep(2)

    led.duty_u16(40000)
    time.sleep(2)

    led.duty_u16(65535)
    time.sleep(2)

    led.duty_u16(0)
    time.sleep(2)
