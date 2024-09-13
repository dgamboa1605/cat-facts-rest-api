from managers.api_manager import APIManager
from models.fact.fact import Fact
from models.fact.response.fact_response import FactResponse
from typing import List


class FactManager(APIManager):

    def get_random_fact(self) -> Fact:
        response = self._make_request("GET", "/facts/random")
        return Fact(**response)

    def get_all_facts(self) -> List[Fact]:
        response = self._make_request("GET", "/facts")
        return [Fact(**fact) for fact in response]

    def get_fact_by_id(self, fact_id: str) -> FactResponse:
        response = self._make_request("GET", f"/facts/{fact_id}")
        return FactResponse(**response)
