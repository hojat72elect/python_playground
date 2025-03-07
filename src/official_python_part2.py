def fibunacci_sequence(n: int):
    """
    You give this function a number and it returns the fibunacci sequence up to that number.
    """
    output_series = [0, 1]
    while output_series[-1] < n:
        output_series.append(output_series[-1] + output_series[-2])
    if output_series[-1] > n:
        output_series.pop()

    return output_series


def input_analyzer():
    """
    will ask you to give it an integer and will print out some info according to what you have entered as input
    """
    print("Let's play a 'guess the number' game")
    try:
        user_input = int(input("please give me an integer number : "))
    except ValueError:
        print("Oh dude! i asked you to enter an integer !!!!")
        return

    if user_input > 42:
        print("The number I have in mind is less than what you have entered.")
    elif user_input < 42:
        print("The number I had in mind is bigger than what you entered.")
    else:
        print("congratulations! you guessed correctly! The number was 42!!!")


if __name__ == '__main__':
    # print(fibunacci_sequence(1_000_000))
    input_analyzer()
