"""
This is a Cython implementation of a prime number finder.
The logic is exactly like the python equivalent, just the implementation is in another language.
"""
def get_primes(int n):
    cdef int i, j
    cdef list primes = []
    cdef int num = 2

    while len(primes) < n:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1

    return primes