def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


primes = [n for n in range(2, 11) if is_prime(n)]
print(primes)
