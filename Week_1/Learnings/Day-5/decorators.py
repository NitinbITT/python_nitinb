# def sum(a, b, mul):
#     return mul(a, b) * (a + b)


# def mul(a, b):
#     return a * b


# print(sum(2, 3, mul))


# def authenticate(func):
#     def process():
#         dictionary = func()
#         if (
#             dictionary.get("name") == "Alex"
#             and dictionary.get("password") == "qwerty123"
#         ):
#             return True
#         else:
#             return False

#     return process


# @authenticate
# def get_user_input():
#     name = "Alex"
#     password = "qwerty123"

#     return {"name": name, "password": password}


# print(get_user_input())


def authenticate(func):
    def process(session):
        dictionary = func(session)
        if (
            dictionary.get("name") == "Alex"
            and dictionary.get("password") == "qwerty123"
            and session != ""
        ):
            return True
        else:
            return False

    return process


@authenticate
def get_user_input(session):
    name = "Alex"
    password = "qwerty123"

    return {"name": name, "password": password}


print(get_user_input("Session32"))
