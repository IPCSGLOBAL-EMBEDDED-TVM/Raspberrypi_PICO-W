import uasyncio as asyncio
from machine import Pin

led = Pin(15, Pin.OUT)

async def blink():
    while True:
        led.toggle()
        await asyncio.sleep_ms(500)

asyncio.run(blink())
