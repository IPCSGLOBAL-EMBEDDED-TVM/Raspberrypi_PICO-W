from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)
address = 0x68

# Wake up MPU6050
i2c.writeto_mem(address, 0x6B, b'\x00')

def read_word(reg):
    data = i2c.readfrom_mem(address, reg, 2)
    value = (data[0] << 8) | data[1]
    return value - 65536 if value > 32767 else value

while True:
    ax = read_word(0x3B)
    ay = read_word(0x3D)
    az = read_word(0x3F)
    print("Accel:", ax, ay, az)
    time.sleep(0.5)
