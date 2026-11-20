from machine import I2C, Pin
import ssd1306
import time

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("Raspberry Pi", 0, 0)
oled.text("Pico W", 0, 16)
oled.text("MicroPython", 0, 32)
oled.show()

while True:
    time.sleep(1)
