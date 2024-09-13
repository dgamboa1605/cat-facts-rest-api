
import requests

from config import config
from typing import Optional


class APIManager:

    def _make_request(self, method: str,
                      endpoint: str,
                      data: Optional[dict] = None,
                      params: Optional[dict] = None):
        url = f"{config.URI}{endpoint}"
        response = requests.request(
            method, url, json=data, params=params, timeout=config.REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()
