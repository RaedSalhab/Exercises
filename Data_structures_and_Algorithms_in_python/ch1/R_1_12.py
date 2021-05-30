"""R-1.12 Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module in-
cludes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function."""

import random

def rand_select(data):
    if len(data) == 0:
        raise IndexError('Cannot choose from an empty sequence')
    return data[random.randrange(len(data))]

if __name__ == '__main__':

    print(rand_select([1, 2, 3, 5, 6]))
    print(rand_select('test'))
