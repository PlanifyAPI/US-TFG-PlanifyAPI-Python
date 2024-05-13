"""
This module provides a rate limiter decorator function.
"""

import time
from functools import wraps
from typing import Callable, List, Any


def rate_limited(calls_per_second: float) -> Callable:
    """
    Decorator function that limits the rate at which a function can be called.

    Args:
        calls_per_second (float): The maximum number of calls allowed per second.

    Returns:
        Callable: The decorated function.

    Example:
        @rate_limited(2)
        def my_function():
            print("Hello, World!")

        my_function()  # This function can be called at most 2 times per second.
    """

    min_interval: float = 1.0 / calls_per_second

    def decorate(func: Callable) -> Callable:
        last_time_called: List[float] = [0.0]

        @wraps(func)
        def rate_limited_func(*args, **kwargs) -> Any:
            elapsed: float = time.perf_counter() - last_time_called[0]
            print("Elapsed:", elapsed)
            remaining_time: float = min_interval - elapsed
            print("Remaining time:", remaining_time)
            if remaining_time > 0:
                print("Sleeping...")
                time.sleep(remaining_time)
            last_time_called[0] = time.perf_counter()
            print(last_time_called)
            return func(*args, **kwargs)

        return rate_limited_func

    return decorate
