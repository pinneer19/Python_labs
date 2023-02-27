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
