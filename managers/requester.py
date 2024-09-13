"""
This module defines the abstract base class `Requester` for handling HTTP requests.
The `Requester` class outlines the methods that must be implemented by any concrete 
class that provides functionality for sending HTTP GET and POST requests.
"""

from abc import ABC, abstractmethod
from typing import Optional

import requests


class Requester(ABC):
    """
    Abstract base class for handling HTTP requests.

    This class defines the interface for sending HTTP GET and POST requests. Any concrete
    class that inherits from `Requester` must implement the `get` and `post` methods.
    """

    @abstractmethod
    def get(self, endpoint: str, params: Optional[dict] = None) -> requests.Response:
        """
        Sends an HTTP GET request to the specified endpoint.

        Args:
            endpoint (str): The URL endpoint to send the request to.
            params (Optional[dict]): Optional dictionary of query parameters to include in the 
                                     request.

        Returns:
            requests.Response: The HTTP response object returned by the request.
        """

    @abstractmethod
    def post(self, endpoint: str, data: Optional[dict] = None) -> requests.Response:
        """
        Sends an HTTP POST request to the specified endpoint.

        Args:
            endpoint (str): The URL endpoint to send the request to.
            data (Optional[dict]): Optional dictionary of data to include in the request body.

        Returns:
            requests.Response: The HTTP response object returned by the request.
        """
