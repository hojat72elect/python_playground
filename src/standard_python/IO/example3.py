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
