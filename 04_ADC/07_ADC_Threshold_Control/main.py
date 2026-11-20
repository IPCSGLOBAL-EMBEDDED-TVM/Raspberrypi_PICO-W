from machine import ADC, Pin
import time

adc = ADC(Pin(26))
led = Pin(15, Pin.OUT)
threshold = 32768

while True:
    value = adc.read_u16()
    led.value(value > threshold)
    print("ADC:", value, "LED:", led.value())
    time.sleep(0.1)
