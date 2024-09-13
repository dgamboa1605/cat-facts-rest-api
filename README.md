
# API Testing Framework

## Overview

This framework is designed for automated API testing. It integrates clean code practices and design patterns such as dependency injection and separation of concerns to ensure maintainability and scalability. It utilizes:
- **Python** as the programming language.
- **Pytest** as the testing framework.
- **Allure** for test reporting.
- **Pylint** for linting and enforcing code quality.

The framework includes components for handling requests, logging, validation, and executing test cases with parameterization and fixtures.

## Table of Contents
1. [Framework Structure](#framework-structure)
2. [Installation](#installation)
3. [Running the Tests](#running-the-tests)
4. [Generating Allure Reports](#generating-allure-reports)
5. [Code Linting](#code-linting)
6. [Test Cases](#test-cases)
7. [Future Improvements](#future-improvements)

## Framework Structure

```
cat-facts-rest-api/
│
├── config/
│   └── config.py        # Configuration details such as URL, timeout, log settings.
│
├── managers/
│   ├── api_requester.py  # Class for making API requests.
│   ├── fact_manager.py   # Class for interacting with the fact API.
│   └── requester.py      # Abstract class for handling HTTP requests.
│
├── models/
│   ├── fact/             # Fact and related models.
│   └── user/             # User and name models.
│
├── tests/
│   ├── conftest.py       # Pytest fixtures for initializing tests.
│   └── test_fact_manager.py  # Test cases for the FactManager class.
│
├── utilities/
│   ├── logger.py         # Logger setup for the project.
│   ├── validators/       # Validation utilities for API responses.
│   └── utils.py          # Utility functions for common tasks.
│
├── pytest.ini            # Pytest configuration, including Allure report directory.
├── logs/                 # Log files generated during test runs.
└── README.md             # This file.
```

### Design Patterns Used
- **Factory Pattern**: The `APIRequester` class serves as a factory for generating HTTP requests.
- **Validation Layer**: The `response_validator.py` module validates API responses against the Pydantic models.
- **Logging**: A custom logger is implemented in `logger.py` to log test activities.

---

## Installation

1. **Clone the repository**:
    ```bash
    git clone git@github.com:dgamboa1605/cat-facts-rest-api.git
    cd cat-facts-rest-api
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Allure Report Setup**:
    - You need to install Allure command-line tool to generate reports.
    - Follow instructions [here](https://allurereport.org/docs/#_get_started).

## Running the Tests

To run the tests with `pytest`, navigate to the project root directory and use the following command:

```bash
pytest
```

Alternatively, if you want to include Allure report generation:

```bash
pytest --alluredir=reports
```

---

## Generating Allure Reports

After running tests, you can generate and view an Allure report:

1. **Generate the report**:
    ```bash
    allure serve reports
    ```

---

## Code Linting

To maintain code quality, `pylint` is used. Run the following command to check the code quality:

```bash
pylint managers/ models/ tests/ utilities/
```

---

## Test Cases

Here is an example of the test cases for validating the API response using the `FactManager`:

| Test Case Name             | Description                                       | Expected Outcome                   |
|----------------------------|---------------------------------------------------|------------------------------------|
| `test_get_fact_by_id`       | Validate retrieving a fact by its ID.             | Fact with the provided ID is returned. |
| `test_get_random_fact`      | Validate retrieval of a random fact from the API. | A random fact is returned.         |
| `test_get_all_facts`        | Validate retrieving all available facts.          | A list of facts is returned.       |
| `test_get_all_facts_with_params`        | Validate retrieving all available facts with parameters: Params: {"animal_type": "cat", "amount": 2}          | A list of 2 facts with `cat` type       |
| `test_get_random_fact_status_code_200`        | Validate response status code.          | Status code 200       |

## Validation Techniques Used

In this framework, we used the **Pydantic** library to validate API responses. Pydantic ensures that the JSON data returned by the API matches the expected structure of our data models (e.g., `Fact`, `FactResponse`). This type of validation is crucial because:
1. It enforces strict type checking, reducing the chance of errors due to unexpected data.
2. It simplifies the process of serializing and deserializing API data, providing a consistent structure to work with.
3. **ID Validation**: Ensures the retrieved fact has the correct ID.
4. **Non-Null Validation**: Checks that essential fields like `text` are not null.
5. **Type Validation**: In cases like `animal_type`, the type is checked against the provided parameters to ensure correctness.
6. **Status Code Validation**: Checks the status code in responses.

These validations are used to ensure the accuracy of the API response, making sure it adheres to expected formats and values.


## Future Improvements

### CI/CD Integration:

In the future, we can integrate this framework into a CI/CD pipeline (e.g., GitLab CI, Jenkins) to automate the test execution and reporting. This will allow continuous testing and feedback for every code change.

#### Example `.gitlab-ci.yml` configuration:

```yaml
image: python:3.8

stages:
  - lint
  - test

before_script:
  - pip install -r requirements.txt

lint:
  stage: lint
  script:
    - pylint pages/

test:
  stage: test
  script:
    - pytest --alluredir=reports
  artifacts:
    paths:
      - reports/
```

### Scalability:

We can enhance this framework by adding support for additional API endpoints, increasing test coverage, and improving performance.

--- 
