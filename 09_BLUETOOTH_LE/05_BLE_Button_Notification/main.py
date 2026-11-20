import bluetooth
import time
from machine import Pin
from micropython import const

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)

SERVICE = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef0")
CHAR = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef1")

ble = bluetooth.BLE()
ble.active(True)
((handle,),) = ble.gatts_register_services((
    (SERVICE, ((CHAR, bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY),)),
))

button = Pin(14, Pin.IN, Pin.PULL_UP)
connections = set()

def irq(event, data):
    if event == _IRQ_CENTRAL_CONNECT:
        connections.add(data[0])
    elif event == _IRQ_CENTRAL_DISCONNECT:
        connections.discard(data[0])

ble.irq(irq)
name = b'PicoW_Button'
adv = bytearray(b'\x02\x01\x06')
adv += bytes([len(name) + 1, 0x09]) + name
ble.gap_advertise(100000, adv_data=adv)

last = button.value()

while True:
    current = button.value()
    if current != last:
        last = current
        value = b'PRESSED' if current == 0 else b'RELEASED'
        ble.gatts_write(handle, value)
        for conn in connections:
            ble.gatts_notify(conn, handle, value)
    time.sleep_ms(50)
