"""
Here we will compare the speed of our function being implemented in 2 different languages(Python and Cython)

"""
import cython_prime_finder
import time
import simple_python_prime_finder

if __name__ == '__main__':
    number_of_primes = 250_000

    # first lets measure the implementation time of the standard_python function
    start_time_python = time.time()
    simple_python_prime_finder.get_primes(number_of_primes)
    stop_time_python = time.time()

    print(f"the standard_python function took {stop_time_python-start_time_python} seconds to run")

    # Now measure the cython function
    start_time_cython = time.time()
    cython_prime_finder.get_primes(number_of_primes)
    stop_time_cython = time.time()

    print(f"the cython function on the other hand, took {stop_time_cython-start_time_cython} seconds")

