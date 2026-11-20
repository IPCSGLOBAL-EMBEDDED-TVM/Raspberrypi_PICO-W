import network
import time

SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_WIFI_PASSWORD"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

for _ in range(20):
    if wlan.isconnected():
        break
    print("Connecting...")
    time.sleep(1)

if wlan.isconnected():
    print("Connected:", wlan.ifconfig())
else:
    print("Connection failed")
