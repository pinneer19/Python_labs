# Calculate some operation with two numbers
def calculate(a, b, op):
    if not all(isinstance(x, int) for x in [a, b]):
        return "Error"

    division, multiply, addition, subtraction = "div", "mult", "add", "sub"
    
    return a / b if op == division \
        else a * b if op == multiply \
        else a + b if op == addition \
        else a - b if op == subtraction \
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

