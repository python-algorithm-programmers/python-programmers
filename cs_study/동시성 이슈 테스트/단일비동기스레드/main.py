import asyncio
counter = 0
no_lock_counter= 0
lock = asyncio.Lock()


async def inc():
	global counter
	for _ in range(1000_000):
		async with lock:
			counter += 1

async def no_lock_inc():
    global no_lock_counter
    for _ in range(1000_000):
        no_lock_counter += 1

async def lock_main():
    await asyncio.gather(inc(), inc())
    await asyncio.gather(no_lock_inc(), no_lock_inc())
    print(f"couter = {counter}")
    print(f"no_lock_counter = {no_lock_counter}")

asyncio.run(lock_main())