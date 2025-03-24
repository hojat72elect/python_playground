import math

if __name__ == '__main__':
    # various kinds of string representation in Python
    string_example1 = "Hello, world."
    print(string_example1)

    print(str(string_example1))

    print(repr(string_example1))

    print(str(1 / 7))

    x = 10 * 3.25
    y = 200 * 200
    string_example2 = f"The value of x is {repr(x)}, and y is {repr(y)}..."
    print(string_example2)

    # The repr() of a string, adds quotes and backslashes.
    hello = 'hello, world\n'
    hellos = repr(hello)
    print(hellos)

    # The argument to repr() may be any kind of python object:
    print(repr((x, y, ('spam', 'eggs'))))

    # Yet another example of formatted strings in Python
    print(f"The value of Pi rounded 3 places after the decimal point is approximately {math.pi:.3f}.")

    # We can use professionally formatted strings for making columns line up in complex printings
    table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 7678}
    for name, phone in table.items():
        print(f"{name:10}  ==> {phone:10d}")
