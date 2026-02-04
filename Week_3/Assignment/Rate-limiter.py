from Exception_rate_limit import RateLimitException
import time


def limit_rate(limit, time_interval):
    class RateLimiter:
        def __init__(self, func):
            self.func = func
            self.limit = limit
            self.time_interval = time_interval
            self.first_call_time = time.perf_counter()
            self.call_count = 0

        def __call__(self, *args, **kwargs):
            current_time = time.perf_counter()

            if current_time - self.first_call_time >= self.time_interval:
                self.call_count = 0
                self.first_call_time += self.time_interval

            if self.call_count >= self.limit:
                raise RateLimitException(
                    " Rate limit exceeded. Please try again later."
                )

            self.call_count += 1
            return self.func(*args, **kwargs)

    return RateLimiter


if __name__ == "__main__":

    @limit_rate(3, 5)
    def request():
        print("API call executed successfully...")


request()
time.sleep(2)
request()
request()
request()
request()
