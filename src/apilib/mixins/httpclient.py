from .event_loop import loop
import aiohttp

__all__ = ("session",)


class _Session:
    def __init__(self):
        self.session = loop.run_until_complete(self._get_session())

    async def _get_session(self):
        return aiohttp.ClientSession()

    def __del__(self):
        if not self.session.closed:
            loop.run_until_complete(self.session.close())

_session = _Session()
session = _session.session