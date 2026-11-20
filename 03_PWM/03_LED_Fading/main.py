from machine import Pin, PWM
import time

led = PWM(Pin(15))
led.freq(1000)

while True:
    for duty in range(0, 65536, 512):
        led.duty_u16(duty)
        time.sleep_ms(10)

    for duty in range(65535, -1, -512):
        led.duty_u16(duty)
        time.sleep_ms(10)
