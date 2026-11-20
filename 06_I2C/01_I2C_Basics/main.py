from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)

while True:
    print("I2C devices:", [hex(x) for x in i2c.scan()])
    time.sleep(2)
