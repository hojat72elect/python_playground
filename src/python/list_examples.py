"""
Here we will play with the most important stuff we can do to a python list.
"""


def list_example_1():
    my_favorite_foods: list[str] = ['pizza', 'chocolate', 'ice cream', 'cookies']
    print(my_favorite_foods)

    my_favorite_foods.append("candy")
    print(my_favorite_foods)

    my_favorite_foods.extend(("fish and chips", "macaroni"))
    print(my_favorite_foods)

    print(my_favorite_foods.pop())
    print(my_favorite_foods.pop())
    print(my_favorite_foods.pop())

    print(my_favorite_foods)

    my_favorite_foods.insert(2, "chicken and rice")
    print(my_favorite_foods)

    my_favorite_foods.remove("ice cream")
    print(my_favorite_foods)

    print(my_favorite_foods.pop(1))
    print(my_favorite_foods)

    my_favorite_foods.clear()
    print(my_favorite_foods)

def list_example_2():
    my_favorite_colors =["cyan", "green", "dark blue", "yellow"]
    print(my_favorite_colors)

    print(my_favorite_colors.index("yellow"))
    print(my_favorite_colors.index("green"))

    my_favorite_colors.append("cyan")
    print(my_favorite_colors)

    print(my_favorite_colors.count("cyan"))
    print(my_favorite_colors.count("yellow"))
    print(my_favorite_colors.count("red"))

    my_favorite_colors.sort()
    print(my_favorite_colors)

    my_favorite_colors.reverse()
    print(my_favorite_colors)

    copy_of_my_favorite_colors = my_favorite_colors.copy()
    print("Before clearing my list, I made a shallow copy of it.")
    my_favorite_colors.clear()
    print(f"Now I have cleared my list and it is like this : {my_favorite_colors}")
    print(f"But the copy I had taken from it is like this : {copy_of_my_favorite_colors}")

if __name__ == '__main__':
    # list_example_1()
    list_example_2()
