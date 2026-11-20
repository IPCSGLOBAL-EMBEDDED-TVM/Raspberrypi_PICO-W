import bluetooth
import time

ble = bluetooth.BLE()
ble.active(True)

def callback(event, data):
    if event == 5:
        addr_type, addr, adv_type, rssi, adv_data = data
        print("Address:", bytes(addr), "RSSI:", rssi,
              "Data:", bytes(adv_data))

ble.irq(callback)
ble.gap_scan(10000, 30000, 30000)

while True:
    time.sleep(1)
