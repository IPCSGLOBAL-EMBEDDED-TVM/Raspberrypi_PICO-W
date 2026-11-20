from machine import Pin, PWM
import time

buzzer = PWM(Pin(16))

frequencies = [500, 700, 900, 1200, 1500]

for frequency in frequencies:
    buzzer.freq(frequency)
    buzzer.duty_u16(32768)
    time.sleep(0.5)
    buzzer.duty_u16(0)
    time.sleep(0.2)

buzzer.deinit()
