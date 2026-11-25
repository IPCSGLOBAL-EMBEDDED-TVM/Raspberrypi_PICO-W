import bluetooth
import time
from machine import Pin

ble = bluetooth.BLE()
ble.active(True)

led = Pin("LED", Pin.OUT)

SERVICE_UUID = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef0")
CHAR_UUID = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef1")

CHAR = (
    CHAR_UUID,
    bluetooth.FLAG_READ | bluetooth.FLAG_WRITE,
)

SERVICE = (
    SERVICE_UUID,
    (CHAR,),
)

((char_handle,),) = ble.gatts_register_services((SERVICE,))


def irq(event, data):
    if event == 1:
        print("Connected")

    elif event == 2:
        print("Disconnected")
        advertise()


def advertise():
    name = "Pico_W"

    payload = bytearray()
    payload += bytes([2, 0x01, 0x06])
    payload += bytes([len(name) + 1, 0x09])
    payload += name.encode()

    ble.gap_advertise(100000, payload)


ble.irq(irq)

advertise()

print("BLE started")
print("Device: Pico_W")

while True:
    try:
        value = ble.gatts_read(char_handle)

        if value == b"1":
            led.on()
            print("LED ON")

            # Clear received value
            ble.gatts_write(char_handle, b"")

        elif value == b"0":
            led.off()
            print("LED OFF")

            ble.gatts_write(char_handle, b"")

    except:
        pass

    time.sleep(0.1)
