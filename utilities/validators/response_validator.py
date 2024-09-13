"""
Module to validate the response of the api requests.
"""

import json

from typing import Any
from pydantic import ValidationError
from utilities.logger import Logger

logger = Logger(__name__)


def validate_response_json(response: Any, model: Any) -> bool:
    """
    Validate the JSON response against the provided Pydantic model.

    Args:
        response (Any): The response object that should have a `.json()` method returning JSON data.
        model (Any): The Pydantic model class to validate the JSON data against.

    Returns:
        bool: True if validation is successful, False otherwise.
    """
    try:
        response_json = response.json()
        logger.info(f"Validating response JSON: {response_json}")
        if isinstance(response_json, list):
            for item in response_json:
                logger.debug(f"Validating item: {item}")
                model(**item)
        else:
            logger.debug(f"Validating response: {response_json}")
            model(**response_json)
        logger.info("Validation successful")
        return True
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        return False
    except ValidationError as e:
        logger.error(f"Pydantic validation error: {e}")
        return False
