import functools
import time
from enum import Enum
from threading import Lock


class Period(int):
    SECOND = 1
    MINUTE = 60
    HOUR = 3600
    DAY = 24 * 3600
    WEEK = 7 * 24 * 3600
    MONTH = 30 * 24 * 3600
    YEAR = 365 * 24 * 3600

class RateLimiter:
    def __init__(self, rate: float, per: int):
        self.rate = rate
        self.per = per
        self.allowance = rate
        self.last_check = time.monotonic()
        self.lock = Lock()

    def acquire(self) -> bool:
        with self.lock:
            current = time.monotonic()
            time_passed = current - self.last_check
            self.last_check = current
            self.allowance += time_passed * (self.rate / self.per)

            if self.allowance > self.rate:
                self.allowance = self.rate

            if self.allowance < 1.0:
                return False

            self.allowance -= 1.0
            return True

def rate_limited(rate: float, per: int):
    rate_limiter = RateLimiter(rate, per)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if rate_limiter.acquire():
                return func(*args, **kwargs)
            else:
                return "Rate limit exceeded. Action not allowed.", 429
        return wrapper
    return decorator