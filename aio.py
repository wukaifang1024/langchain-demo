import asyncio


async def main():
    print('---------sleep start-------')
    await asyncio.sleep(3)
    print('---------sleep end-------')

    print('---------gather start-------')
    result = await asyncio.gather(task1(), task2())
    print('---------gather end-------')
    print(result)


async def task1():
    print('task1 start')
    await asyncio.sleep(1)
    print('task1 end')
    return 'task1'


async def task2():
    print('task2 start')
    await asyncio.sleep(3)
    print('task2 end')
    return 'task2'

if __name__ == '__main__':
    asyncio.run(main())



