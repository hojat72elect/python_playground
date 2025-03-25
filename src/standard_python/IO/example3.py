if __name__ == '__main__':
    # An example of how to use other modifiers to convert string before formatting it
    animals = "eels"
    print(f"My hovercraft is full of {animals}.")
    print(f"My hovercraft is full of {animals!r}.")

    # Using = in a formatted string
    bugs = 'flies'
    count = 13
    area = 'living room'
    print(f"Debugging {bugs=} {count=} {area=}")

    # Using the format() function on a String
    print("We are the {} who say '{}!'".format('knights', 'Ni'))

    # Second example
    print("{0} and {1}".format("spam", "eggs"))

    # Third example
    print("{1} and {0}".format("spam", "eggs"))

    # Fourth example
    print("this {food} is {adjective}.".format(food="spam", adjective="absolutely horrible"))

    # Fifth example
    print("The story of {0}, {1}, and {other}.".format("Bill", "Manfred", other="Georg"))

    # Sixth example
    table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
    print("Jack : {0[Jack]:d}; Sjoerd : {0[Sjoerd]:d}; Dcab : {0[Dcab]:d}".format(table))

    # Seventh example
    print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

    # Eighth example (Prints out a dictionary containing all local variables)
    second_table = {k: str(v) for k, v in vars().items()}
    message = " ".join([f'{k}: ' + '{' + k + '};' for k in second_table.keys()])
    print(message.format(**second_table))

    # A clean table of number, their squares, and their cubes
    for x in range(1, 11):
        print("{0:2d} {1:3d} {2:4d}".format(x, x ** 2, x ** 3))
