"""
This module contains test cases for the FactManager class.
"""

import pytest
import allure

from managers.fact_manager import FactManager
from models.fact.fact import Fact
from utilities.validators.response_validator import validate_response_json
from utilities.logger import Logger


@allure.feature("Fact Manager")
@pytest.mark.usefixtures("fact_manager")
class TestFactManager:
    """
    Test suite for the FactManager class.
    """

    fact_manager: FactManager = None
    logger = Logger(__name__)

    @pytest.fixture(autouse=True)
    def setup(self, fact_manager) -> None:
        """
        Fixture to set up the FactManager instance for each test.

        Args:
            fact_manager (FactManager): The FactManager instance provided by pytest fixtures.
        """
        self.fact_manager = fact_manager

    @allure.title("Get Fact by ID")
    @pytest.mark.parametrize("fact_id", ["58e008780aac31001185ed05"])
    def test_get_fact_by_id(self, fact_id):
        """
        Test case to verify retrieval of a fact by its ID.

        Args:
            fact_id (str): The ID of the fact to retrieve.

        Raises:
            AssertionError: If the fact is not found or its attributes do not match expectations.
        """
        self.logger.info(
            f"Starting test_get_fact_by_id with fact_id: {fact_id}")
        fact = self.fact_manager.get_fact_by_id(fact_id)
        assert fact is not None, f"Expected fact but got None for ID: {fact_id}"
        assert fact.id == fact_id, f"Expected ID: {fact_id}, but got: {fact.id}"
        assert fact.text is not None, "Fact text should not be None"
        self.logger.info(f"Successfully retrieved fact with ID: {fact_id}")

    @allure.title("Get Random Fact")
    def test_get_random_fact(self):
        """
        Test case to check retrieval of a random fact.

        Raises:
            AssertionError: If the random fact is not found or its attributes are not as expected.
        """
        self.logger.info("Starting test_get_random_fact")
        fact = self.fact_manager.get_random_fact()
        assert fact is not None, "Expected a fact but got None"
        assert fact.id is not None, "Random fact should have a valid ID"
        assert fact.text is not None, "Random fact should have a non-null text"
        self.logger.info("Successfully retrieved random fact")

    @allure.title("Get Random Fact with Parameters")
    def test_get_random_fact_with_params(self):
        """
        Test case to validate retrieval of random facts with specified parameters.

        Raises:
            AssertionError: If the facts do not meet the specified parameters or 
                            if the list length is not as expected.
        """
        params = {"animal_type": "cat", "amount": 2}
        self.logger.info(
            f"Starting test_get_random_fact_with_params with parameters: {params}")
        facts = self.fact_manager.get_random_fact(params=params)
        assert facts is not None, "Expected a list of facts but got None"
        assert len(facts) == 2, f"Expected 2 facts, but got: {len(facts)}"
        for fact in facts:
            assert fact.type == "cat", f"Each fact should have type cat, but got:{fact.type}"
        self.logger.info("Successfully retrieved random facts with parameters")

    @allure.title("Verify Status Code 200 for Random Fact")
    def test_get_random_fact_status_code_200(self):
        """
        Test case to confirm that the random fact API returns a status code 200.

        Raises:
            AssertionError: If the status code returned is not 200.
        """
        self.logger.info("Starting test_get_random_fact_status_code_200")
        response = self.fact_manager.requester.get("/facts/random")
        assert response.status_code == 200, f"Expected 200, but got: {response.status_code}"
        self.logger.info("Status code 200 verified for random fact request")

    @allure.title("Validate Random Fact Response")
    def test_get_random_fact_valid_response(self):
        """
        Test case to ensure that the response from the random fact API is valid.

        Raises:
            AssertionError: If the response does not match the expected schema or is invalid.
        """
        self.logger.info("Starting test_get_random_fact_valid_response")
        response = self.fact_manager.requester.get("/facts/random")
        assert validate_response_json(
            response, Fact), "Expected a valid response, but got invalid"
        self.logger.info("Random fact response validated")

    @allure.title("Get All Facts")
    def test_get_all_facts(self):
        """
        Test case to verify retrieval of all facts.

        Raises:
            AssertionError: If the facts list is empty or 
                            any fact does not meet the expected criteria.
        """
        self.logger.info("Starting test_get_all_facts")
        facts = self.fact_manager.get_all_facts()
        assert facts is not None, "Expected a list of facts but got None"
        assert len(facts) > 0, "Expected at least one fact, but got an empty list"
        for fact in facts:
            assert fact.id is not None, "Each fact should have a valid ID"
            assert fact.text is not None, "Each fact should have non-null text"
        self.logger.info("Successfully retrieved all facts")

    @allure.title("Get All Facts with Parameters")
    def test_get_all_facts_with_params(self):
        """
        Test case to validate retrieval of all facts with specified parameters.

        Raises:
            AssertionError: If the facts do not meet the specified parameters or 
                            if the list is empty.
        """
        params = {"animal_type": "cat,horse"}
        self.logger.info(
            f"Starting test_get_all_facts_with_params with parameters: {params}")
        facts = self.fact_manager.get_all_facts(params=params)
        assert facts is not None, "Expected a list of facts but got None"
        assert len(facts) > 0, "Expected at least one fact, but got an empty list"
        for fact in facts:
            assert fact.type is not None, "Each fact should have non-null type"
            assert fact.type in [
                "cat", "horse"], f"Each fact should have type as: cat, horse, but got{fact.type}"
        self.logger.info("Successfully retrieved all facts with parameters")
