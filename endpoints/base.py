import requests
from support.logger import log_func


class BaseAPI:
    LOG = log_func()

    def __init__(self, session: requests.Session, url: str):
        self.session = session
        self.url = url

    def get(self, *args, **kwargs):
        response = self.session.get(*args, **kwargs)
        self.LOG.info(f"Send get request to {self.url}")
        return response


