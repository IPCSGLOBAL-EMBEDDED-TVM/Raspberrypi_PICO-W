import uasyncio as asyncio
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
