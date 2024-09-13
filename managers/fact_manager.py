"""
This module contains the FactManager class, which provides methods to interact with a fact API. 
The FactManager class is used to fetch random facts, all facts, and specific facts by ID.
"""

from typing import List, Optional
from managers.requester import Requester
from models.fact.fact import Fact
from models.fact.response.fact_response import FactResponse
from utilities.validators.response_validator import validate_response_json
from utilities.logger import Logger


class FactManager:
    """
    Manages interactions with the fact API.
    """

    logger = Logger(__name__)

    def __init__(self, requester: Requester) -> None:
        self.requester = requester

    def get_random_fact(self, params: Optional[dict] = None) -> Fact:
        """
        Fetches a random fact from the API.

        Args:
            params (Optional[dict]): Optional parameters to include in the request.

        Returns:
            Fact: An instance of the Fact class containing the random fact.

        Raises:
            ValueError: If the response from the API is invalid.
        """
        self.logger.info(f"Fetching random fact with params: {params}")
        response = self.requester.get("/facts/random", params=params)
        if validate_response_json(response, Fact):
            if params is not None:
                facts = [Fact(**fact) for fact in response.json()]
                self.logger.info(f"Retrieved {len(facts)} facts")
                return facts
            fact = Fact(**response.json())
            self.logger.info(f"Retrieved fact response with text: {fact.text}")
            return fact
        self.logger.error("Invalid response format for random fact")
        raise ValueError("Invalid response")

    def get_all_facts(self, params: Optional[dict] = None) -> List[Fact]:
        """
        Fetches all facts from the API.

        Args:
            params (Optional[dict]): Optional parameters to include in the request.

        Returns:
            List[Fact]: A list of Fact instances containing all the facts.

        Raises:
            ValueError: If the response from the API is invalid.
        """
        self.logger.info(f"Fetching all facts with params: {params}")
        response = self.requester.get("/facts", params=params)
        if validate_response_json(response, Fact):
            facts = [Fact(**fact) for fact in response.json()]
            self.logger.info(f"Retrieved {len(facts)} facts")
            return facts
        self.logger.error("Invalid response format for random fact")
        raise ValueError("Invalid response")

    def get_fact_by_id(self, fact_id: str) -> FactResponse:
        """
        Fetches a fact by its ID from the API.

        Args:
            fact_id (str): The ID of the fact to fetch.

        Returns:
            FactResponse: An instance of the FactResponse class containing the fact details.

        Raises:
            ValueError: If the response from the API is invalid.
        """
        self.logger.info(f"Fetching fact by ID: {fact_id}")
        response = self.requester.get(f"/facts/{fact_id}")
        if validate_response_json(response, FactResponse):
            fact_response = FactResponse(**response.json())
            self.logger.info(f"Retrieved fact response with text: {fact_response.text}")
            return fact_response
        self.logger.error("Invalid response format for fact by ID")
        raise ValueError("Invalid response")
