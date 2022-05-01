from .mixins.httpclient import session
from .mixins.event_loop import loop


class API:
    def __init__(self, url, authentication: dict = None, async_mode: bool = True):
        self.url = url
        self.auth = authentication

        if async_mode:
            self.get = self._get
            self.post = self._post
        else:
            self.get = self._sync_get
            self.post = self._sync_post

    def _sync_get(self, endpoint: str, content_type: str, params: dict = None, headers: dict = None):
        return loop.run_until_complete(self._get(endpoint, content_type, params, headers))

    def _sync_post(self, endpoint: str, data: dict, content_type: str, params: dict = None, headers: dict = None):
        return loop.run_until_complete(self._post(endpoint, data, content_type, params, headers))

    async def _get(self, endpoint: str, content_type: str, params: dict = None, headers: dict = None):
        url = self.url
        if tuple(self.url)[-1] == "/":
            url += endpoint[1:]
        else:
            url += endpoint

        async with session.get(url, auth=self.auth, headers=headers, params=params) as response:
            if content_type == "json":
                return await response.json()
            else:
                return await response.text()

    async def _post(self, endpoint: str, data: dict, content_type: str, params: dict = None, headers: dict = None):
        url = self.url
        if tuple(self.url)[-1] == "/":
            url += endpoint[1:]
        else:
            url += endpoint

        async with session.post(url, auth=self.auth, headers=headers, params=params, data=data) as response:
            if content_type == "json":
                return await response.json()
            else:
                return await response.text()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, trace):
        pass