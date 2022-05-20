import asyncio


async def task(x):
    for i in range(3):
        print('Task{0} is Running'.format(x))

cor = task(1)

# loop = asyncio.get_event_loop()
# ret = loop.run_until_complete(cor)
# print(ret)
asyncio.run(cor)