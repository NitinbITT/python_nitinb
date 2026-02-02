import time


def check_runtime(Function):
    def calculate_runtime(value1, value2):
        start_time = time.perf_counter()
        multiply_value = Function(value1, value2)
        end_time = time.perf_counter()
        print(
            f"Function {Function.__name__} took {end_time-start_time:.4f} seconds to execute"
        )
        return multiply_value

    return calculate_runtime


@check_runtime
def multiply(number1, number2):
    time.sleep(2)
    return number1 * number2


print("Result:", multiply(2, 3))
