"""
R-6.5 Implement a function that reverses a list of elements by pushing them onto
    a stack in one order, and writing them back to the list in reversed order.
"""

from array_stak import ArratStak

def reverse_list(data):
    rev_data = []
    S = ArratStak()
    for e in data:
        S.push(e)
    
    while not S.is_empty():
        item = S.pop()
        rev_data.append(item)

    return rev_data


if __name__ == '__main__':
    print(reverse_list([1, 2, 3, 4, 5, 6, 7]))
