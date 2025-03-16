import itertools
from typing import Iterator, Generator


def iterator_example():
    example_data: list[int] = [1, 2, 4, 8]
    example_iterator: Iterator[int] = iter(example_data)

    print(example_data)
    print(example_iterator.__next__())
    print(example_iterator.__next__())
    print(example_iterator.__next__())
    print(example_iterator.__next__())
    # print(example_iterator.__next__()) # This line will throw an error


def generator_example() -> Generator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    iterator_example()

    # First example of how to use our generator:
    generator1 = generator_example()
    for _ in range(10):
        print(next(generator1))

    # Second example of how to use our generator:
    generator2 = generator_example()
    fibonacci_sequence_list: list[int] = [next(generator2) for _ in range(15)]
    print(fibonacci_sequence_list)

    # Third example of how to use our generator:
    generator3 = generator_example()
    for num in itertools.islice(generator3, 20):  # use islice to limit the number of iterations
        print(num)

    # Fourth example of how to use our generator:
    generator4 = generator_example()
    for num in generator4:
        if num > 100:
            break
        print(num)
