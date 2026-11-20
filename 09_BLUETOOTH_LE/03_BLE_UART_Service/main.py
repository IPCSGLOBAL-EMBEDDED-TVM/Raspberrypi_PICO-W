import bluetooth
import time
from micropython import const

_IRQ_WRITE = const(3)
_UART_UUID = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
_TX_UUID = bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")
_RX_UUID = bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")

UART_SERVICE = (
    _UART_UUID,
    (
        (_TX_UUID, bluetooth.FLAG_NOTIFY),
        (_RX_UUID, bluetooth.FLAG_WRITE),
    ),
)

ble = bluetooth.BLE()
ble.active(True)
((tx_handle, rx_handle),) = ble.gatts_register_services((UART_SERVICE,))

def irq(event, data):
    if event == _IRQ_WRITE:
        conn_handle, value_handle = data
        if value_handle == rx_handle:
            print("BLE RX:", ble.gatts_read(rx_handle))

ble.irq(irq)

name = b'PicoW_UART'
adv = bytearray(b'\x02\x01\x06')
adv += bytes([len(name) + 1, 0x09]) + name
ble.gap_advertise(100000, adv_data=adv)

while True:
    time.sleep(1)
