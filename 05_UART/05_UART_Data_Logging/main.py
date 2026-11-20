from machine import UART, Pin
import time

uart = UART(0, 115200, tx=Pin(0), rx=Pin(1))
count = 0

while True:
    count += 1
    message = "Sample," + str(count) + "\r\n"
    uart.write(message)
    time.sleep(1)
