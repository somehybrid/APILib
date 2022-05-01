import asyncio

loop = asyncio.get_event_loop()

def run(coro):
    try:
        loop.run_until_complete(coro)
    except TypeError:
        loop.run_until_complete(coro())