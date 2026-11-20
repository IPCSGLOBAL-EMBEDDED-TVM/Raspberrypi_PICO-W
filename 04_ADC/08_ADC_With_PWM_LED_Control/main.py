from machine import ADC, Pin, PWM
import time

adc = ADC(Pin(26))
led = PWM(Pin(15))
led.freq(1000)

while True:
    value = adc.read_u16()
    led.duty_u16(value)
    print("ADC:", value)
    time.sleep_ms(20)
