import asyncio


async def gzq():
    return 21


async def main():
    task = asyncio.create_task(gzq())
    done, pending = await asyncio.wait((task, ))

    if task in done:
        print(f'Task Result is {task.result()}')

asyncio.run(main())