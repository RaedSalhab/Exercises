"""R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function."""

import R_1_4

def total_sum2(n):
    return R_1_4.total_sum(n)


if __name__ == '__main__':
    print(total_sum2(1))
    print(total_sum2(2))
    print(total_sum2(3))
    print(total_sum2(4))
    print(total_sum2(5))
