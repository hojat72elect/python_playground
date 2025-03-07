def else_in_for_loop_example():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n // x)
                break
        else:
            # Loop fell through without finding a factor
            print(n, 'is a prime number')


def match_case_example(http_error_code: int):
    match http_error_code:
        case 400:
            print("Bad request")
        case 404:
            print("Not found")
        case 418:
            print("I'm a teapot")
        case 401 | 402 | 403:
            print("This http request is not allowed")
        case _:
            print("Something is wrong with the internet")


if __name__ == '__main__':
    # else_in_for_loop_example()
    match_case_example(402)
