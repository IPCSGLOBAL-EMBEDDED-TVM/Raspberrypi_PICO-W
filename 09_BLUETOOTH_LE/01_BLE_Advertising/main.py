import bluetooth
import time

ble = bluetooth.BLE()
ble.active(True)

name = b'PicoW_BLE'
payload = bytearray(b'\x02\x01\x06')
payload += bytes([len(name) + 1, 0x09]) + name

ble.gap_advertise(100000, adv_data=payload)

while True:
    time.sleep(1)
