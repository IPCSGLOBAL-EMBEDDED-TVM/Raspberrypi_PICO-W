from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(5), sda=Pin(4))
address = 0x68

i2c.writeto_mem(address, 0x6B, b'\x00')
time.sleep_ms(100)

value = i2c.readfrom_mem(address, 0x6B, 1)
print("Register 0x6B:", value[0])
