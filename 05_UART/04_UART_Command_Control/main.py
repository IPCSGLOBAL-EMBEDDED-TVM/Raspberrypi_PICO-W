from machine import UART, Pin
import time

uart = UART(0, 9600, tx=Pin(0), rx=Pin(1))
led = Pin(15, Pin.OUT)

while True:
    if uart.any():
        command = uart.read().strip().upper()
        if command == b'ON':
            led.on()
            uart.write("LED ON\r\n")
        elif command == b'OFF':
            led.off()
            uart.write("LED OFF\r\n")
        else:
            uart.write("Use ON or OFF\r\n")
    time.sleep_ms(20)
