"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""


def add(a, b):
    """Add two numbers together"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    print(f"Multiplying {a} × {b}")
    result = a * b
    print(f"Result: {result}")
    return result


def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")

    # FIX for Test Case: The test expects a simpler message.
    if b == 0:
        raise ValueError("Cannot divide by zero")

    print(f"Dividing {a} ÷ {b}")
    result = a / b
    print(f"Result: {result}")
    return result


def power(a, b):
    """Raise a to the power of b"""
    return a ** b


def square_root(a):
    """Calculate square root of a"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5


if __name__ == "__main__":
    print("🧮 Calculator Module")
    # Basic Operations
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    # Example usage for new functions
    print(f"3 * 4 = {multiply(3, 4)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"2 ** 3 = {power(2, 3)}")
    print(f"√9 = {square_root(9)}")