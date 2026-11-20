from machine import Pin, PWM
import time

buzzer = PWM(Pin(16))

buzzer.freq(1000)
buzzer.duty_u16(32768)
time.sleep(1)

buzzer.duty_u16(0)
buzzer.deinit()
