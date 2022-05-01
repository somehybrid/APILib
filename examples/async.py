import apilib

async def test():
    api = apilib.API("https://httpbin.org/", async_mode=False)
    print(api.get("/get", "json"))

apilib.run(test())