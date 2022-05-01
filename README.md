# APILib

A simple Python library to access APIs


[![Built with Python](https://img.shields.io/badge/-Python-22496a?style=for-the-badge&logo=Python&logoColor=white)](https://www.python.org)
[![Built with Aiohttp](https://img.shields.io/badge/-Aiohttp-FFFFFF?style=for-the-badge&logo=Aiohttp&logoColor=blue)](https://docs.aiohttp.org/en/stable/)

## Features

- Fast API
- Supports async/await syntax
- Simple to use

## Installation

**Python 3.6 or higher is required**

To install APILib, run
```
pip install apilib
```

## Examples

### Example 1 (async mode off)
```python
import apilib

api = apilib.API("https://httpbin.org/", async_mode=False)
print(api.get("/get", "json"))
```

### Example 2 (async mode on)
```python
import apilib

async def test():
    api = apilib.API("https://httpbin.org/", async_mode=False)
    print(api.get("/get", "json"))

apilib.run(test())
```
* Note: to use asyncio. use `apilib.run()` or `apilib.loop` as asyncio does not allow use of multiple event loops.

Find more examples in the examples directory
