#! /usr/bin/env python3.7

import time
import asyncio


async def count():
    print('🐜')
    await asyncio.sleep(1)
    print('⚛')


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(elapsed)
