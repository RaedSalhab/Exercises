"""R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n."""

def total_sum(n):
    n =abs(n)
    result = 0
    for num in range(1, n):
        result = result + (num * num)
    return result


if __name__ == '__main__':
    print(total_sum(1))
    print(total_sum(2))
    print(total_sum(3))
    print(total_sum(4))
    print(total_sum(5))
