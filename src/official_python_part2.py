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

if __name__ == '__main__':
    print(fibunacci_sequence(1_000_000))
