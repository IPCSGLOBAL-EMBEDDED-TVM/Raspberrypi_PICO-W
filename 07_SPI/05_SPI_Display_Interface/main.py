from machine import SPI, Pin
import time

spi = SPI(0, baudrate=8000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))

cs = Pin(17, Pin.OUT, value=1)
dc = Pin(20, Pin.OUT)

def send_data(data):
    dc.value(1)
    cs.value(0)
    spi.write(data)
    cs.value(1)

def send_command(command):
    dc.value(0)
    cs.value(0)
    spi.write(bytes([command]))
    cs.value(1)

# Example transfer only. Initialize your display
# using its controller-specific command sequence.
send_command(0x00)
send_data(b'Pico W SPI')
