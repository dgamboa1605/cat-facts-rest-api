"""
This module contains a pytest fixture for initializing the FactManager with 
an APIRequester and a Logger.
"""

import pytest
from managers.fact_manager import FactManager
from managers.api_requester import APIRequester
from utilities.logger import Logger

logger = Logger(__name__)

@pytest.fixture(scope="function")
def fact_manager():
    """
    This fixture sets up the FactManager with an instance of APIRequester. 

    Returns:
        FactManager: An instance of FactManager initialized with APIRequester.
    """
    api_requester = APIRequester()
    logger.info("Initializing FactManager with APIRequester.")
    fact_manager_instance = FactManager(api_requester)
    logger.info("FactManager initialized successfully.")
    return fact_manager_instance
