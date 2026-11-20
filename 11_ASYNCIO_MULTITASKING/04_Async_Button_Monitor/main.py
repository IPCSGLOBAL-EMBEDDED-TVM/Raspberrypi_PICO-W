import uasyncio as asyncio
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
