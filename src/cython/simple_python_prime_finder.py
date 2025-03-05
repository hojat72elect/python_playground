"""
This function is pure python for finding the first n prime numbers.
"""
def get_primes(n):
    if n < 1:
        return []

    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1

    return primes
