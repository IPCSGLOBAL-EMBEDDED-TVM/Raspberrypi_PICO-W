import uasyncio as asyncio

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
