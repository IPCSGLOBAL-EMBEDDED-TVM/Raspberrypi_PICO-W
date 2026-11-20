import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

for item in wlan.scan():
    print("SSID:", item[0].decode(), "RSSI:", item[3])
