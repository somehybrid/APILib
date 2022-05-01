import apilib

async def test():
    with apilib.API("https://httpbin.org/") as api:
        print(await api.get("/get", "json"))

apilib.run(test())