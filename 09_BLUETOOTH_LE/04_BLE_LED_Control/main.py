import bluetooth
import time
from machine import Pin
from micropython import const

_IRQ_WRITE = const(3)
SERVICE = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef0")
CHAR = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef1")

ble = bluetooth.BLE()
ble.active(True)
((handle,),) = ble.gatts_register_services((
    (SERVICE, ((CHAR, bluetooth.FLAG_WRITE),)),
))

led = Pin(15, Pin.OUT)

def irq(event, data):
    if event == _IRQ_WRITE:
        conn, value_handle = data
        if value_handle == handle:
            command = ble.gatts_read(handle).strip().upper()
            if command == b'ON':
                led.on()
            elif command == b'OFF':
                led.off()

ble.irq(irq)
name = b'PicoW_LED'
adv = bytearray(b'\x02\x01\x06')
adv += bytes([len(name) + 1, 0x09]) + name
ble.gap_advertise(100000, adv_data=adv)

while True:
    time.sleep(1)
