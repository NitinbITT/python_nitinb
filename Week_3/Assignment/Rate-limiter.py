import time


class rate_limit:
    def __init__(self, func):
        self.func = func
        self.limit = 3
        self.time_interval = 5
        self.call_count = 0
        self.prev_time = time.perf_counter()

    def __call__(self, *args, **kwargs):
        current_time = time.perf_counter()

        if current_time - self.prev_time > self.time_interval:
            self.prev_time = current_time
            self.call_count = 0

        if self.call_count >= self.limit:
            print("Error occurred: Rate limit exceeded. Please try again later.")
            return

        self.call_count += 1
        return self.func(*args, **kwargs)


@rate_limit
def request():
    print("API call executed successfully...")

request()
time.sleep(5)
request()
request()
request()
request()
