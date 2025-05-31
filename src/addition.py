# app.py
# This is a test commit
# hello world

import sys

def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(5, 2) == 7

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python app.py <num1> <num2>")
        sys.exit(1)

    # Convert command line arguments to integers
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("Please provide two integer arguments.")
        sys.exit(1)

    result = add(num1, num2)
    print(f"Result: {result}")
