from machine import SPI, Pin
import time

spi = SPI(0, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))

cs = Pin(17, Pin.OUT, value=1)

while True:
    cs.value(0)
    spi.write(b'Hello')
    cs.value(1)
    time.sleep(1)
