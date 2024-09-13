import pytest
from managers.fact_manager import FactManager

fact_manager = FactManager()

@pytest.mark.parametrize("fact_id", ["58e008780aac31001185ed05"])
def test_get_fact_by_id(fact_id):
    fact = fact_manager.get_fact_by_id(fact_id)
    assert fact.id == fact_id

def test_get_random_fact():
    fact = fact_manager.get_random_fact()
    assert fact.text is not None

def test_get_all_facts():
    facts = fact_manager.get_all_facts()
    assert len(facts) > 0
