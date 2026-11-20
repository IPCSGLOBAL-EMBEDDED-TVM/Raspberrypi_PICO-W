from machine import Pin, PWM
import time

pwm = PWM(Pin(15))
pwm.freq(1000)
pwm.duty_u16(32768)

while True:
    time.sleep(1)
