from machine import Pin, PWM
import time

servo = PWM(Pin(17))
servo.freq(50)

def set_angle(angle):
    pulse_us = 500 + (angle / 180) * 2000
    duty = int(pulse_us * 65535 / 20000)
    servo.duty_u16(duty)

while True:
    for angle in [0, 45, 90, 135, 180]:
        set_angle(angle)
        time.sleep(1)

    for angle in [180, 135, 90, 45, 0]:
        set_angle(angle)
        time.sleep(1)
