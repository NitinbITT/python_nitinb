def count(start):
    while 1:
        start += 1
        yield start


timer = count(2)
print(next(timer))
print(next(timer))
