import apilib

with apilib.API("https://httpbin.org/", async_mode=False) as api:
    print(api.get("/get", "json"))