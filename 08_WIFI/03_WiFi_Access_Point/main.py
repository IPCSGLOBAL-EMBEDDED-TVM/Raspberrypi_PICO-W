import network
import time

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(ssid="PicoW_AP", password="pico12345")

while not ap.active():
    time.sleep(0.1)

print("AP active:", ap.ifconfig())
