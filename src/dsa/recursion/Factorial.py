def factorial(n: int) -> int:
    """
    Returns the factorial of n.
    n must be a non-negative integer.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    example1 = 2
    example2 = 4
    example3 = 6
    example4 = 10

    print(f"The factorial of {example1} is {factorial(example1)}")
    print(f"The factorial of {example2} is {factorial(example2)}")
    print(f"The factorial of {example3} is {factorial(example3)}")
    print(f"The factorial of {example4} is {factorial(example4)}")