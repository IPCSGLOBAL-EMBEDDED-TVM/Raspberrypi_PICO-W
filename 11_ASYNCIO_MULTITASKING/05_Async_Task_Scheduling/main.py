import uasyncio as asyncio

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
