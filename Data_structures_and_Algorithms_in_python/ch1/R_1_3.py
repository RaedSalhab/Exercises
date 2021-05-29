"""R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""

def minmax(data):
    smallest, largest = data[0], data[0]
    for num in data[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest


if __name__ == '__main__':
    print(minmax([1]))
    print(minmax([12, 34, 87, 44, 223, 757, 2]))
    print(minmax([125, 54, 5234, 667, 8635456, 543]))
    print(minmax([125, 54, 5234, 667, -8635456, 543]))
