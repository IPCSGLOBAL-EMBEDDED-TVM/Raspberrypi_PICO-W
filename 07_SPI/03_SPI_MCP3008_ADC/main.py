from machine import SPI, Pin
import time

spi = SPI(0, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs = Pin(17, Pin.OUT, value=1)

def read_adc(channel):
    if not 0 <= channel <= 7:
        raise ValueError("Channel must be 0 to 7")
    tx = bytearray([1, (8 + channel) << 4, 0])
    rx = bytearray(3)
    cs.value(0)
    spi.write_readinto(tx, rx)
    cs.value(1)
    return ((rx[1] & 3) << 8) | rx[2]

while True:
    print("CH0:", read_adc(0))
    time.sleep(0.5)
