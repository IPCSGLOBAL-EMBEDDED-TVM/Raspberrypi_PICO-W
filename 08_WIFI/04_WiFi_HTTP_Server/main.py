import network
import socket
import time

SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_WIFI_PASSWORD"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(1)

print("IP:", wlan.ifconfig()[0])

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(addr)
server.listen(1)

while True:
    client, remote = server.accept()
    request = client.recv(1024)
    response = b'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Pico W Server</h1>'
    client.send(response)
    client.close()
