# -*- coding: utf-8 -*-

import asyncio
import time

loop = asyncio.get_event_loop()


async def hello():
    print('111111')
    await asyncio.sleep(5)
    print('111111Hello World:%s' % time.time())


async def hello2():
    print('222222')
    await asyncio.sleep(10)
    print('222222Hello World:%s' % time.time())


async def hello3():
    print('33333')
    await asyncio.sleep(20)
    print('33333Hello World:%s' % time.time())

tasks = [
    asyncio.ensure_future(hello()),
    asyncio.ensure_future(hello2()),
    asyncio.ensure_future(hello3())
]
loop.run_until_complete(asyncio.wait(tasks))
