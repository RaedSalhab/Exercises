"""R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n."""

def sum_square_odd(n):
    n = abs(n)
    result = 0
    for num in range(1, n):
        if num % 2 == 1:
            result += pow(num, 2)
    return result

if __name__ == '__main__':

    test = {}
    for i in range(10):
        test.update({i: sum_square_odd(i)})

    print(test)
