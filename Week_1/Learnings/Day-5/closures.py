def outer_func():
    a = 10

    def inner_func():
        b = 50

        def inner_func_2():
            return a * b

        return inner_func_2

    return inner_func


func = outer_func()
func2 = func()

print(func2())
