from machine import UART, Pin
import time

uart = UART(0, 9600, tx=Pin(0), rx=Pin(1))

uart.write("AT\r\n")

while True:
    if uart.any():
        print(uart.read())
    time.sleep_ms(50)
