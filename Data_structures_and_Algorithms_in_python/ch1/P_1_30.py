"""P-1.30 Write a Python program that can take a positive integer greater
than 2 as input and write out the number of times one must repeatedly divide
this number by 2 before getting a value less than 2."""

def dividing(num):
    repeated = 0
    if num < 0 or not isinstance(num, int):
        raise TypeError('The number must positive integer.')

    while num > 2:
        num = num // 2
        repeated += 1

    return repeated

if __name__ == '__main__':
    print(dividing(2))
    print(dividing(5))
    print(dividing(6))
    print(dividing(9))
    print(dividing(10))
