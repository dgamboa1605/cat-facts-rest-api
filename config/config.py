"""
A configuration class for setting up the browser and test environment.

URL (str): The base URL of the application under test. Default is the Twitch mobile site.
REQUEST_TIMEOUT (int): The time to wait until raise an error in request.
LOG_LEVEL (str): The level of logging to be used (e.g., DEBUG, INFO). Default is "DEBUG".
LOG_NAME (str): The name of the log file.
"""

URI = "https://cat-fact.herokuapp.com"
REQUEST_TIMEOUT = 10
LOG_LEVEL = "DEBUG"
LOG_NAME = "log_file.log"
