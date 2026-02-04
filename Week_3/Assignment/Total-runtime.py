import time


def check_runtime(function):
    def calculate_runtime(*args, **kwargs):
        start_time = time.perf_counter()
        multiply_value = function(*args, **kwargs)
        end_time = time.perf_counter()
        print(
            f"Function {function.__name__} took {end_time-start_time:.4f} seconds to execute"
        )
        return multiply_value

    return calculate_runtime


@check_runtime
def multiply(number1, number2):
    return number1 * number2


print("Result:", multiply(2, 3))
