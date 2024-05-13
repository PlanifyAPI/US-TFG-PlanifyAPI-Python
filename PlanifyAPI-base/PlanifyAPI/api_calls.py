"""
This module provides a class for making API calls.
"""

import json
import os
from datetime import datetime, timedelta

import requests


class APICall:
    """
    A class for making API calls.

    Attributes:
        url (str): The URL of the API endpoint.
        method (str): The HTTP method to use for the API call.
        headers (dict): The headers to include in the API call.
        body (str): The body of the API call.

    Methods:
        execute(): Executes the API call and returns the response.
        get_calls_per_second(rate, time_unit): Calculates the number of calls per second given a rate and time unit.
        log_request(response=None): Logs the API call request.
    """

    def __init__(
        self, name: str, url: str, method: str, headers: dict = None, body: str = None
    ) -> None:
        self.name = name
        self.url = url
        self.method = method
        self.headers = headers
        self.body = body
        self.request_count = 0

    def execute(self) -> requests.Response:
        """
        Executes the API call and returns the response.

        Returns:
            requests.Response: The response object.
        """
        self.request_count += 1
        response = requests.request(
            self.method, self.url, headers=self.headers, data=self.body, timeout=25
        )
        self.log_request(response)
        return response

    def get_calls_per_second(self, rate: float, time_unit: timedelta) -> float:
        """
        Calculates the number of calls per second given a rate and time unit.

        Args:
            rate (float): The rate of calls.
            time_unit (timedelta): The time unit in which the rate is measured.

        Returns:
            float: The number of calls per second.
        """
        return rate / time_unit.total_seconds()

    def log_request(self, response: requests.Response = None) -> None:
        """
        Logs the API call request.

        Args:
            response (requests.Response): The response object.
        """
        log_data = {}
        error_codes = [
            400,
            401,
            402,
            403,
            404,
            405,
            406,
            407,
            408,
            409,
            410,
            411,
            412,
            413,
            414,
            415,
            416,
            417,
            418,
            421,
            422,
            423,
            424,
            425,
            426,
            428,
            429,
            431,
            451,
            500,
            501,
            502,
            503,
            504,
            505,
            506,
            507,
            508,
            510,
            511,
        ]

        log_data["timestamp"] = int(datetime.now().timestamp())

        if response is None or response.status_code in error_codes:
            log_data["level"] = "ERROR"
            log_data["description"] = (
                f"API: {self.name}:{self.request_count} - Response: {response.status_code}"
            )
        else:
            log_data["level"] = "INFO"
            log_data["description"] = (
                f"API: {self.name}:{self.request_count} - Response: {response.status_code}"
            )

        log_directory = f"log/{self.name}"
        os.path.exists(log_directory) or os.makedirs(log_directory)
        with open(
            f"{log_directory}/{self.name}_filtered.json", "a", encoding="utf-8"
        ) as log_file:
            log_file.write(json.dumps(log_data) + "\n")
