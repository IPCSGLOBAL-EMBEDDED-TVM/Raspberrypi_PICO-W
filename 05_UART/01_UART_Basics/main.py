from machine import UART, Pin
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
    uart.write("Hello from Pico W\r\n")
    time.sleep(1)
