
from pathlib import Path

ROOT = Path(".")

# Each experiment contains:
# folder, objective, wiring, source code

sections = {
"04_ADC": [
("01_ADC_Basics", "Read raw ADC values from an analog input.",
 "Connect a potentiometer wiper to GP26/ADC0. Connect its outer terminals to 3V3 and GND.",
"""from machine import ADC, Pin
import time

adc = ADC(Pin(26))

while True:
    value = adc.read_u16()
    print("ADC:", value)
    time.sleep(0.5)
"""),
("02_Potentiometer_Reading", "Read a potentiometer and observe its changing ADC value.",
 "Potentiometer outer terminals: 3V3 and GND. Wiper: GP26/ADC0.",
"""from machine import ADC, Pin
import time

pot = ADC(Pin(26))

while True:
    print("Potentiometer:", pot.read_u16())
    time.sleep(0.2)
"""),
("03_ADC_Voltage_Conversion", "Convert ADC readings into an approximate voltage.",
 "Connect potentiometer wiper to GP26/ADC0; outer terminals to 3V3 and GND.",
"""from machine import ADC, Pin
import time

adc = ADC(Pin(26))
VREF = 3.3

while True:
    raw = adc.read_u16()
    voltage = raw * VREF / 65535
    print("Raw:", raw, "Voltage:", round(voltage, 3), "V")
    time.sleep(0.5)
"""),
("04_Internal_Temperature_Sensor", "Read the RP2040 internal temperature sensor.",
 "No external sensor required. The internal sensor is ADC channel 4.",
"""from machine import ADC
import time

sensor = ADC(4)

while True:
    voltage = sensor.read_u16() * 3.3 / 65535
    temperature = 27 - (voltage - 0.706) / 0.001721
    print("Approx. chip temperature:", round(temperature, 2), "C")
    time.sleep(2)
"""),
("05_LDR_Light_Sensor", "Measure light-dependent voltage using an LDR voltage divider.",
 "Use an LDR and 10k resistor as a divider between 3V3 and GND. Connect their junction to GP27/ADC1.",
"""from machine import ADC, Pin
import time

ldr = ADC(Pin(27))

while True:
    print("Light level:", ldr.read_u16())
    time.sleep(0.5)
"""),
("06_Analog_Sensor_Reading", "Read an analog sensor output.",
 "Connect a 3.3V-compatible analog sensor output to GP28/ADC2. Connect sensor GND to Pico GND.",
"""from machine import ADC, Pin
import time

sensor = ADC(Pin(28))

while True:
    raw = sensor.read_u16()
    voltage = raw * 3.3 / 65535
    print("Sensor:", raw, "Voltage:", round(voltage, 3))
    time.sleep(0.5)
"""),
("07_ADC_Threshold_Control", "Switch an LED when an analog input crosses a threshold.",
 "Potentiometer wiper to GP26; outer terminals to 3V3/GND. LED on GP15 through a 220-330 ohm resistor.",
"""from machine import ADC, Pin
import time

adc = ADC(Pin(26))
led = Pin(15, Pin.OUT)
threshold = 32768

while True:
    value = adc.read_u16()
    led.value(value > threshold)
    print("ADC:", value, "LED:", led.value())
    time.sleep(0.1)
"""),
("08_ADC_With_PWM_LED_Control", "Use a potentiometer to continuously control LED brightness.",
 "Potentiometer wiper to GP26; outer terminals to 3V3/GND. LED on GP15 through a resistor.",
"""from machine import ADC, Pin, PWM
import time

adc = ADC(Pin(26))
led = PWM(Pin(15))
led.freq(1000)

while True:
    value = adc.read_u16()
    led.duty_u16(value)
    print("ADC:", value)
    time.sleep_ms(20)
"""),
],

"05_UART": [
("01_UART_Basics", "Transmit text through UART0.",
 "UART0 TX GP0 to USB-UART adapter RX; connect GND. Use 3.3V logic.",
"""from machine import UART, Pin
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
    uart.write("Hello from Pico W\\r\\n")
    time.sleep(1)
"""),
("02_UART_Receive", "Receive serial data through UART0.",
 "USB-UART TX to Pico GP1/RX; connect GND. Adapter must use 3.3V logic.",
"""from machine import UART, Pin
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
    if uart.any():
        data = uart.read()
        print("Received:", data)
    time.sleep_ms(20)
"""),
("03_UART_Two_Way_Communication", "Transmit and receive UART messages.",
 "Connect USB-UART TX to GP1 and GP0 to USB-UART RX. Connect GND.",
"""from machine import UART, Pin
import time

uart = UART(0, 9600, tx=Pin(0), rx=Pin(1))

while True:
    uart.write("Pico W ready\\r\\n")
    if uart.any():
        print("RX:", uart.read())
    time.sleep(1)
"""),
("04_UART_Command_Control", "Control an LED using serial commands.",
 "USB-UART TX to GP1, GP0 to USB-UART RX, common GND. LED on GP15 through resistor.",
"""from machine import UART, Pin
import time

uart = UART(0, 9600, tx=Pin(0), rx=Pin(1))
led = Pin(15, Pin.OUT)

while True:
    if uart.any():
        command = uart.read().strip().upper()
        if command == b'ON':
            led.on()
            uart.write("LED ON\\r\\n")
        elif command == b'OFF':
            led.off()
            uart.write("LED OFF\\r\\n")
        else:
            uart.write("Use ON or OFF\\r\\n")
    time.sleep_ms(20)
"""),
("05_UART_Data_Logging", "Send periodic sensor-style data over UART.",
 "USB-UART RX to GP0/TX and GND to GND.",
"""from machine import UART, Pin
import time

uart = UART(0, 115200, tx=Pin(0), rx=Pin(1))
count = 0

while True:
    count += 1
    message = "Sample," + str(count) + "\\r\\n"
    uart.write(message)
    time.sleep(1)
"""),
("06_UART_External_Device", "Exchange data with an external UART device.",
 "Connect Pico GP0/TX to external RX and GP1/RX to external TX. Common GND; both sides must use compatible 3.3V logic.",
"""from machine import UART, Pin
import time

uart = UART(0, 9600, tx=Pin(0), rx=Pin(1))

uart.write("AT\\r\\n")

while True:
    if uart.any():
        print(uart.read())
    time.sleep_ms(50)
"""),
],

"06_I2C": [
("01_I2C_Basics", "Initialize an I2C bus and scan for connected devices.",
 "Connect device SDA to GP4 and SCL to GP5. Connect GND and suitable supply. Ensure pull-ups are present.",
"""from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)

while True:
    print("I2C devices:", [hex(x) for x in i2c.scan()])
    time.sleep(2)
"""),
("02_I2C_Device_Scan", "Identify I2C device addresses.",
 "Connect an I2C module SDA to GP4 and SCL to GP5, with common GND.",
"""from machine import I2C, Pin

i2c = I2C(0, scl=Pin(5), sda=Pin(4))

devices = i2c.scan()
if devices:
    for address in devices:
        print("Found:", hex(address))
else:
    print("No I2C devices found")
"""),
("03_I2C_OLED_Display", "Display text on an SSD1306 OLED.",
 "SSD1306 SDA to GP4, SCL to GP5, VCC to compatible supply and GND to GND. Install an SSD1306 MicroPython driver as ssd1306.py.",
"""from machine import I2C, Pin
import ssd1306
import time

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("Raspberry Pi", 0, 0)
oled.text("Pico W", 0, 16)
oled.text("MicroPython", 0, 32)
oled.show()

while True:
    time.sleep(1)
"""),
("04_I2C_MPU6050", "Read accelerometer and gyroscope registers from an MPU6050.",
 "MPU6050 SDA to GP4, SCL to GP5, common GND and compatible supply. Address normally 0x68.",
"""from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)
address = 0x68

# Wake up MPU6050
i2c.writeto_mem(address, 0x6B, b'\\x00')

def read_word(reg):
    data = i2c.readfrom_mem(address, reg, 2)
    value = (data[0] << 8) | data[1]
    return value - 65536 if value > 32767 else value

while True:
    ax = read_word(0x3B)
    ay = read_word(0x3D)
    az = read_word(0x3F)
    print("Accel:", ax, ay, az)
    time.sleep(0.5)
"""),
("05_I2C_Register_Read_Write", "Write to and read back an I2C device register.",
 "Connect a compatible I2C device to GP4 SDA and GP5 SCL. This example uses an MPU6050 power-management register.",
"""from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(5), sda=Pin(4))
address = 0x68

i2c.writeto_mem(address, 0x6B, b'\\x00')
time.sleep_ms(100)

value = i2c.readfrom_mem(address, 0x6B, 1)
print("Register 0x6B:", value[0])
"""),
],

"07_SPI": [
("01_SPI_Basics", "Initialize SPI and transmit bytes.",
 "SPI0 SCK GP18, MOSI GP19, MISO GP16. Connect GND. A peripheral must be connected to receive data.",
"""from machine import SPI, Pin
import time

spi = SPI(0, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))

cs = Pin(17, Pin.OUT, value=1)

while True:
    cs.value(0)
    spi.write(b'Hello')
    cs.value(1)
    time.sleep(1)
"""),
("02_SPI_Loopback_Test", "Test SPI transmission using a loopback connection.",
 "Connect GP19/MOSI directly to GP16/MISO. No external peripheral required.",
"""from machine import SPI, Pin
import time

spi = SPI(0, baudrate=100000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))

while True:
    tx = b'PICO'
    rx = bytearray(len(tx))
    spi.write_readinto(tx, rx)
    print("TX:", tx, "RX:", bytes(rx))
    time.sleep(1)
"""),
("03_SPI_MCP3008_ADC", "Read an analog voltage through an MCP3008 SPI ADC.",
 "MCP3008 VDD/VREF to 3.3V, AGND/DGND to GND. Connect CLK GP18, DIN GP19, DOUT GP16, CS GP17. CH0 receives a 0-3.3V signal.",
"""from machine import SPI, Pin
import time

spi = SPI(0, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs = Pin(17, Pin.OUT, value=1)

def read_adc(channel):
    if not 0 <= channel <= 7:
        raise ValueError("Channel must be 0 to 7")
    tx = bytearray([1, (8 + channel) << 4, 0])
    rx = bytearray(3)
    cs.value(0)
    spi.write_readinto(tx, rx)
    cs.value(1)
    return ((rx[1] & 3) << 8) | rx[2]

while True:
    print("CH0:", read_adc(0))
    time.sleep(0.5)
"""),
("04_SPI_EEPROM_Read", "Read data from a 25LC256 SPI EEPROM.",
 "Connect EEPROM CS GP17, SCK GP18, SI/MOSI GP19, SO/MISO GP16. Power and ground according to the chip datasheet. WP and HOLD high.",
"""from machine import SPI, Pin
import time

spi = SPI(0, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs = Pin(17, Pin.OUT, value=1)

def read_status():
    cs.value(0)
    spi.write(b'\\x05')
    result = spi.read(1)
    cs.value(1)
    return result[0]

def read_data(address, length):
    command = bytes([0x03, (address >> 8) & 255, address & 255])
    cs.value(0)
    spi.write(command)
    data = spi.read(length)
    cs.value(1)
    return data

while True:
    print("Status:", hex(read_status()))
    print("Memory:", read_data(0, 16))
    time.sleep(2)
"""),
("05_SPI_Display_Interface", "Understand SPI display communication using an SPI peripheral.",
 "This is an SPI initialization and transfer template. Connect a compatible SPI display's SCK, MOSI, CS, DC, RESET and GND. Display-specific commands are required.",
"""from machine import SPI, Pin
import time

spi = SPI(0, baudrate=8000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))

cs = Pin(17, Pin.OUT, value=1)
dc = Pin(20, Pin.OUT)

def send_data(data):
    dc.value(1)
    cs.value(0)
    spi.write(data)
    cs.value(1)

def send_command(command):
    dc.value(0)
    cs.value(0)
    spi.write(bytes([command]))
    cs.value(1)

# Example transfer only. Initialize your display
# using its controller-specific command sequence.
send_command(0x00)
send_data(b'Pico W SPI')
"""),
],

"08_WIFI": [
("01_WiFi_Scan", "Scan for nearby Wi-Fi networks.",
 "No external hardware required. Run in a location with Wi-Fi signals.",
"""import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

for item in wlan.scan():
    print("SSID:", item[0].decode(), "RSSI:", item[3])

"""),
("02_WiFi_Connect", "Connect Pico W to a Wi-Fi access point.",
 "Enter your own Wi-Fi SSID and password in the program.",
"""import network
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
"""),
("03_WiFi_Access_Point", "Configure Pico W as a Wi-Fi access point.",
 "No external hardware required. Connect a phone or computer to the created network.",
"""import network
import time

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(ssid="PicoW_AP", password="pico12345")

while not ap.active():
    time.sleep(0.1)

print("AP active:", ap.ifconfig())
"""),
("04_WiFi_HTTP_Server", "Serve a simple web page from the Pico W.",
 "Connect Pico W to Wi-Fi. Update SSID and password. Open its IP address in a browser.",
"""import network
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
    response = b'HTTP/1.0 200 OK\\r\\nContent-Type: text/html\\r\\n\\r\\n<h1>Pico W Server</h1>'
    client.send(response)
    client.close()
"""),
("05_WiFi_Time_NTP", "Synchronize the Pico W clock using an NTP server.",
 "Connect Pico W to internet-enabled Wi-Fi. Update credentials.",
"""import network
import ntptime
import time

SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_WIFI_PASSWORD"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(1)

ntptime.settime()
print("UTC time:", time.localtime())
"""),
("06_WiFi_UDP_Communication", "Send a UDP message over Wi-Fi.",
 "Connect Pico W and the receiving computer to the same Wi-Fi network. Replace DEST_IP with the receiver's IP.",
"""import network
import socket
import time

SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_WIFI_PASSWORD"
DEST_IP = "192.168.1.100"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(1)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    sock.sendto(b'Hello from Pico W', (DEST_IP, 5005))
    time.sleep(2)
"""),
],

"09_BLUETOOTH_LE": [
("01_BLE_Advertising", "Advertise the Pico W as a BLE device.",
 "No external hardware required. Scan using a phone BLE scanner app.",
"""import bluetooth
import time

ble = bluetooth.BLE()
ble.active(True)

name = b'PicoW_BLE'
payload = bytearray(b'\\x02\\x01\\x06')
payload += bytes([len(name) + 1, 0x09]) + name

ble.gap_advertise(100000, adv_data=payload)

while True:
    time.sleep(1)
"""),
("02_BLE_Scan", "Scan for nearby BLE advertising devices.",
 "No external hardware required. BLE scanning support depends on the installed MicroPython firmware.",
"""import bluetooth
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
"""),
("03_BLE_UART_Service", "Create a BLE UART-style GATT service for receiving and sending text.",
 "Use a BLE client such as nRF Connect. Connect to PicoW_UART and use the RX characteristic to write data.",
"""import bluetooth
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
adv = bytearray(b'\\x02\\x01\\x06')
adv += bytes([len(name) + 1, 0x09]) + name
ble.gap_advertise(100000, adv_data=adv)

while True:
    time.sleep(1)
"""),
("04_BLE_LED_Control", "Control an LED using a BLE GATT write characteristic.",
 "Connect using nRF Connect. Write ASCII ON or OFF to the writable characteristic. LED on GP15 through resistor.",
"""import bluetooth
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
adv = bytearray(b'\\x02\\x01\\x06')
adv += bytes([len(name) + 1, 0x09]) + name
ble.gap_advertise(100000, adv_data=adv)

while True:
    time.sleep(1)
"""),
("05_BLE_Button_Notification", "Send button state updates using BLE notifications.",
 "Button GP14 to GND with pull-up. Connect a BLE client and enable notifications on the characteristic.",
"""import bluetooth
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
adv = bytearray(b'\\x02\\x01\\x06')
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
"""),
],

"10_TIMERS_INTERRUPTS": [
("01_Hardware_Timer", "Generate periodic events using a hardware timer.",
 "No external hardware required. Optional LED on GP15.",
"""from machine import Pin, Timer
import time

led = Pin(15, Pin.OUT)

def timer_callback(timer):
    led.toggle()

timer = Timer()
timer.init(period=500, mode=Timer.PERIODIC, callback=timer_callback)

while True:
    time.sleep(1)
"""),
("02_Timer_Counter", "Count periodic timer events.",
 "No external hardware required.",
"""from machine import Timer
import time

count = 0

def callback(timer):
    global count
    count += 1

timer = Timer()
timer.init(period=1000, mode=Timer.PERIODIC, callback=callback)

while True:
    print("Timer events:", count)
    time.sleep(2)
"""),
("03_Button_Interrupt", "Detect a button edge using GPIO interrupt handling.",
 "Button GP14 to GND using internal pull-up. LED on GP15 through resistor.",
"""from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)
event = False

def irq_handler(pin):
    global event
    event = True

button.irq(trigger=Pin.IRQ_FALLING, handler=irq_handler)

while True:
    if event:
        event = False
        led.toggle()
        time.sleep_ms(200)
    time.sleep_ms(10)
"""),
("04_Non_Blocking_Task", "Perform periodic operations without blocking delays.",
 "Optional LED on GP15.",
"""from machine import Pin
import time

led = Pin(15, Pin.OUT)
last = time.ticks_ms()
interval = 500

while True:
    now = time.ticks_ms()
    if time.ticks_diff(now, last) >= interval:
        led.toggle()
        last = now
"""),
("05_Multiple_Periodic_Tasks", "Schedule two independent periodic activities using ticks.",
 "LED1 on GP15 and LED2 on GP16, each through a resistor.",
"""from machine import Pin
import time

led1 = Pin(15, Pin.OUT)
led2 = Pin(16, Pin.OUT)

last1 = time.ticks_ms()
last2 = time.ticks_ms()

while True:
    now = time.ticks_ms()

    if time.ticks_diff(now, last1) >= 500:
        led1.toggle()
        last1 = now

    if time.ticks_diff(now, last2) >= 1000:
        led2.toggle()
        last2 = now
"""),
],

"11_ASYNCIO_MULTITASKING": [
("01_Asyncio_Basics", "Run two cooperative asynchronous coroutines.",
 "No external hardware required.",
"""import uasyncio as asyncio

async def task_one():
    while True:
        print("Task one")
        await asyncio.sleep(1)

async def task_two():
    while True:
        print("Task two")
        await asyncio.sleep(2)

async def main():
    asyncio.create_task(task_one())
    asyncio.create_task(task_two())
    while True:
        await asyncio.sleep(10)

asyncio.run(main())
"""),
("02_Async_LED_Blink", "Blink an LED using an asynchronous task.",
 "LED on GP15 through a 220-330 ohm resistor.",
"""import uasyncio as asyncio
from machine import Pin

led = Pin(15, Pin.OUT)

async def blink():
    while True:
        led.toggle()
        await asyncio.sleep_ms(500)

asyncio.run(blink())
"""),
("03_Async_Multiple_LEDs", "Run independent LED tasks concurrently.",
 "LED1 on GP15 and LED2 on GP16 through separate resistors.",
"""import uasyncio as asyncio
from machine import Pin

led1 = Pin(15, Pin.OUT)
led2 = Pin(16, Pin.OUT)

async def blink(led, delay):
    while True:
        led.toggle()
        await asyncio.sleep(delay)

async def main():
    asyncio.create_task(blink(led1, 0.5))
    asyncio.create_task(blink(led2, 1.0))
    while True:
        await asyncio.sleep(5)

asyncio.run(main())
"""),
("04_Async_Button_Monitor", "Monitor a button asynchronously without blocking other tasks.",
 "Button GP14 to GND with internal pull-up. LED GP15 through resistor.",
"""import uasyncio as asyncio
from machine import Pin

button = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)

async def monitor_button():
    last = button.value()
    while True:
        current = button.value()
        if current != last:
            await asyncio.sleep_ms(30)
            current = button.value()
            if current != last:
                last = current
                led.value(0 if current else 1)
        await asyncio.sleep_ms(10)

asyncio.run(monitor_button())
"""),
("05_Async_Task_Scheduling", "Create and schedule multiple asynchronous tasks.",
 "No external hardware required.",
"""import uasyncio as asyncio

async def sensor_task():
    while True:
        print("Reading sensor...")
        await asyncio.sleep(2)

async def communication_task():
    while True:
        print("Communication task running...")
        await asyncio.sleep(3)

async def main():
    asyncio.create_task(sensor_task())
    asyncio.create_task(communication_task())
    while True:
        await asyncio.sleep(10)

asyncio.run(main())
"""),
]
}

def create_experiment(section, item):
    folder, objective, wiring, code = item
    path = ROOT / section / folder
    path.mkdir(parents=True, exist_ok=True)

    (path / "main.py").write_text(code.strip() + "\n")

    readme = f"""# {folder.replace('_', ' ')}

## Objective
{objective}

## Hardware Requirements
- Raspberry Pi Pico W
- Hardware listed in the wiring instructions below

## Wiring
{wiring}

## Source Code
See `main.py`.

## How to Run
1. Connect the Pico W to your computer.
2. Open the project in Thonny or your MicroPython-compatible editor.
3. Upload `main.py` to the Pico W.
4. Run the program.
5. Observe the output in the serial terminal or on the connected hardware.

## Learning Outcomes
- Understand the peripheral or protocol used in this experiment.
- Configure the relevant MicroPython interface.
- Observe the hardware response or serial output.
- Modify the program to explore different configurations.

## Safety Notes
- Pico W GPIO and ADC inputs use 3.3V logic.
- Do not apply 5V to GPIO or ADC pins.
- Check the connected module's voltage requirements.
- Use common ground for external circuits.
"""
    (path / "README.md").write_text(readme)

for section, experiments in sections.items():
    for item in experiments:
        create_experiment(section, item)

    summary = [
        f"# {section.replace('_', ' ')}",
        "",
        "## Overview",
        f"This section contains {len(experiments)} Raspberry Pi Pico W MicroPython experiments.",
        "",
        "## Experiments",
    ]

    for index, item in enumerate(experiments, start=1):
        folder, objective, wiring, code = item
        summary.append(f"{index}. [{folder.replace('_', ' ')}]({folder}/README.md)")

    summary += [
        "",
        "## File Structure",
        "Each experiment folder contains:",
        "- `main.py` - MicroPython source code",
        "- `README.md` - Experiment objective, wiring and instructions",
        "",
        "## Hardware Platform",
        "Raspberry Pi Pico W running MicroPython.",
    ]

    (ROOT / section / "README.md").write_text("\n".join(summary) + "\n")
    print(f"{section}: {len(experiments)} experiments created")

print("\\nAll remaining experiment folders and documentation generated.")
