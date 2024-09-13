"""
This module contains the APIRequester class, which is responsible for making HTTP requests 
to a specified API endpoint. It extends the Requester class.
"""

from typing import Optional

import requests

from config import config
from managers.requester import Requester
from utilities.logger import Logger


class APIRequester(Requester):
    """
    A class responsible for making HTTP requests using the Requests library.
    Inherits from the Requester class and utilizes the Logger for logging purposes.
    """

    logger = Logger(__name__)

    def _make_request(self, method: str, endpoint: str,
                     data: Optional[dict] = None,
                     params: Optional[dict] = None) -> requests.Response:
        """
        Makes an HTTP request to a specified endpoint with optional data and parameters.

        Args:
            method (str): The HTTP method to use for the request (e.g., 'GET', 'POST').
            endpoint (str): The API endpoint to send the request to, appended to the base URI.
            data (Optional[dict], optional): The request body data to send 
                                             (used with methods like POST). Defaults to None.
            params (Optional[dict], optional): The query parameters to include in the request URL. 
                                               Defaults to None.

        Returns:
            requests.Response: The response object from the requests library, 
                               containing the server's response to the HTTP request.
        """
        url = f"{config.URI}{endpoint}"
        self.logger.debug(f"Making {method} request to URL: {url}")
        self.logger.debug(f"Request data: {data}")
        self.logger.debug(f"Request parameters: {params}")
        response = requests.request(
            method, url, json=data, params=params, timeout=config.REQUEST_TIMEOUT)

        return response

    def get(self, endpoint: str, params: Optional[dict] = None) -> requests.Response:
        """
        Convenience method for making GET requests.

        Args:
            endpoint (str): The API endpoint to send the request to.
            params (Optional[dict], optional): The query parameters to include in the request URL. 
                                               Defaults to None.

        Returns:
            requests.Response: The response object from the requests library.
        """
        return self._make_request("GET", endpoint, params=params)

    def post(self, endpoint: str, data: Optional[dict] = None) -> requests.Response:
        """
        Convenience method for making POST requests.

        Args:
            endpoint (str): The API endpoint to send the request to.
            data (Optional[dict], optional): The request body data to send.

        Returns:
            requests.Response: The response object from the requests library.
        """
        return self._make_request("POST", endpoint, data=data)
