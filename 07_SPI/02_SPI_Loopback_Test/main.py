from machine import SPI, Pin
import time

spi = SPI(0, baudrate=100000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))

while True:
    tx = b'PICO'
    rx = bytearray(len(tx))
    spi.write_readinto(tx, rx)
    print("TX:", tx, "RX:", bytes(rx))
    time.sleep(1)
