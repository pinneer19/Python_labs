# Calculate some operation with two numbers
def calculate(num1: int|float, num2: int|float, op: str):

    division, multiply, addition, subtraction = "div", "mult", "add", "sub"

    return num1 / num2 if op == division and num2 != 0 \
        else num1 * num2 if op == multiply \
        else num1 + num2 if op == addition \
        else num1 - num2 if op == subtraction \
        else "Error"
        

# Get even numbers from the given list
def even(numbers_list):
    if not all(isinstance(x, int) for x in numbers_list):
        return "Error"

    result = []

    for i in numbers_list:
        if i % 2 == 0:
            result.append(i)

    return result

