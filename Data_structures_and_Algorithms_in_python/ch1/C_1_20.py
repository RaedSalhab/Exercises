"""C-1.20 Python’srandommodule includes a functionshuffle(data)that accepts
a list of elements and randomly reorders the elements so that each possible
order occurs with equal probability.  Therandommodule includes amore basic
function randint(a, b)that returns a uniformly random integer from a to b
(including both endpoints).Using only therandintfunction,implement your own
version of the shuffle function."""

import random

def my_shuffle(x):
    a = 0
    b = len(x) - 1
    result = []
    for item in x:
        i = random.randint(a, b)
        result.insert(i, item)

    return result

if __name__ == '__main__':
    print(my_shuffle([3, 4, 8, 5, 7]))
    print(my_shuffle([3, 4, 8, 5, 7]))
    print(my_shuffle([3, 4, 8, 5, 7]))
    print(my_shuffle([3, 4, 8, 5, 7]))
