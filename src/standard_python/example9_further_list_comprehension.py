from math import pi

if __name__ == '__main__':
    vec = [-4, -2, 0, 2, 4]

    example_vec1 = [2 * x for x in vec]
    print(example_vec1)

    example_vec2 = [x for x in vec if x >= 0]
    print(example_vec2)

    example_vec3 = [abs(x) for x in vec]
    print(example_vec3)

    fresh_fruits = ['banana', 'long berry', 'passion fruit']
    example_fruits = [fruit.upper() for fruit in fresh_fruits]
    print(example_fruits)

    list_of_number_and_its_square = [(x, x ** 2) for x in range(6)]
    print(list_of_number_and_its_square)

    # You can use list comprehension for flattening a list of lists. but I don't recommend
    original_vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_vector = [num for first_elem in original_vector for num in first_elem]
    print(flattened_vector)

    pi_estimations = [round(pi, i) for i in range(1, 6)]
    print(pi_estimations)

    # This is how you calculate transpose of a matrix in the real world
    initial_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    transposed_matrix = list(zip(*initial_matrix))
    print(transposed_matrix)
