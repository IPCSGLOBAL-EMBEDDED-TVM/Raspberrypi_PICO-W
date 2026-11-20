from machine import UART, Pin
import time

uart = UART(0, 9600, tx=Pin(0), rx=Pin(1))

while True:
    uart.write("Pico W ready\r\n")
    if uart.any():
        print("RX:", uart.read())
    time.sleep(1)
