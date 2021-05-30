"""C-1.15 Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)."""

def distinct_list(data):

    for num in data:
        repeated = data.count(num)
        if repeated > 1:
            return False

    return True

if __name__  == "__main__":
    print(distinct_list([1,2,3,4,5,6,7]))
    print(distinct_list([1,6,3,4,5,6,7]))
    print(distinct_list([5,2,3,5,5,6,7]))
