def perform_general_math_operations():
    number1 = 2
    number2 = 4

    print(f"the result of the addition is {number1 + number2}")
    print(f"the result of the subtraction is {number1 - number2}")
    print(f"the result of the multiplication is {number1 * number2}")
    print(f"the result of the floating point division is {number1 / number2}")
    print(f"the result of the floor division is {number1 // number2}")
    print(f"The remainder of 7 being devided by 3 is {7 % 3}")
    print(f"the floating point result of 7 divided by 3 is {7 / 3}")
    print(f"And the floor division of the same numbers as above is {7 // 3}")
    print(f"In python, we can raise 2 to the power of 5 like this: {2 ** 5}")


def use_a_long_string():
    merged_string = ("Hello world, my name is Hojat;\n"
                     "And so far, I have enjoyed living on this planet.")
    print(merged_string)


def strings_in_python():
    example_string_1 = "Hello world!\nmy name is Hojat."

    # string indexing
    print(example_string_1[0])
    print(example_string_1[5])
    print(example_string_1[-1])
    print(example_string_1[-2])
    print(example_string_1[-6])

    # string slicing
    print(example_string_1[0:2])
    print(example_string_1[2:5])
    print(example_string_1[:2])
    print(example_string_1[4:])
    print(example_string_1[-2:])

    # the built-in function len() works on strings as well
    print(len(example_string_1))


def lists_in_python():
    list_of_squares = [1, 4, 9, 16, 25]
    print(list_of_squares)

    # indexing in lists
    print(list_of_squares[0])
    print(list_of_squares[-1])

    # slicing in lists
    print(list_of_squares[-3:])

    # Concatenating lists together
    print(list_of_squares + [36, 49, 64, 81, 100])

    list_of_squares.append(36)
    print(list_of_squares)

    # be careful of multiple references to the same list:
    second_reference_to_the_list_of_squares = list_of_squares
    print(id(list_of_squares) == id(second_reference_to_the_list_of_squares))
    second_reference_to_the_list_of_squares.append(49)
    print(list_of_squares)

    # The builtin function len() works on lists as well
    print(len(list_of_squares))


if __name__ == '__main__':
    lists_in_python()
