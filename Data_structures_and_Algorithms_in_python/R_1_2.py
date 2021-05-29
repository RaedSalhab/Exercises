"""R-1.2 Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators."""
from R_1_1 import is_multiple

def is_even(k):
    return is_multiple(k, 2)


if __name__ == '__main__':
    print(is_even(10))
    print(is_even(201))
    print(is_even(123))
    print(is_even(26))
