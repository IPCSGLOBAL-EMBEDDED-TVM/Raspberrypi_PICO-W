from machine import I2C, Pin

i2c = I2C(0, scl=Pin(5), sda=Pin(4))

devices = i2c.scan()
if devices:
    for address in devices:
        print("Found:", hex(address))
else:
    print("No I2C devices found")
