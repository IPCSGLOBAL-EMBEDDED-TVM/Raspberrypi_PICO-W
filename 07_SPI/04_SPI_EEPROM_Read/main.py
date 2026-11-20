from machine import SPI, Pin
import time

spi = SPI(0, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs = Pin(17, Pin.OUT, value=1)

def read_status():
    cs.value(0)
    spi.write(b'\x05')
    result = spi.read(1)
    cs.value(1)
    return result[0]

def read_data(address, length):
    command = bytes([0x03, (address >> 8) & 255, address & 255])
    cs.value(0)
    spi.write(command)
    data = spi.read(length)
    cs.value(1)
    return data

while True:
    print("Status:", hex(read_status()))
    print("Memory:", read_data(0, 16))
    time.sleep(2)
