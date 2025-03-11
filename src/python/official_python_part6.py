def function_annotations_example1(first_parameter, second_parameter):
    print(
        f"The function annotations of a vanilla python function is like this : {function_annotations_example1.__annotations__}"
    )

def function_annotations_example2(first_parameter: float, second_parameter: int) -> list[str]:
    print(f"But the function annotations of a python function with annotations is like this : {function_annotations_example2.__annotations__}")


if __name__ == '__main__':
    function_annotations_example1(1, 2)
    function_annotations_example2(1.0, 2)
