def cheeseshop(kind, *available_cheeses, **available_drinks):
    print(f"Do you have any {kind} cheese?")
    print(f"sorry bro! we're all out of {kind}.")

    print(type(available_cheeses))
    for cheese in available_cheeses:
        print(cheese)

    print("And we also have these drinks:")
    print(type(available_drinks))
    for drink in available_drinks:
        print(f"{drink} which was manufactured by {available_drinks[drink]}.")


def example_lambda_usage(n):
    return lambda x: x + n


if __name__ == '__main__':
    cheeseshop("Feta", "German", "Cheddar", "Swiss", shweps="Pilsner", pug="Budweiser")
    incrementor1 = example_lambda_usage(8)
    print(incrementor1(23))
    print(incrementor1(45))
    print(incrementor1(235))
    print(incrementor1(76))
    print(incrementor1(91))
