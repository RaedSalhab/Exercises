"""C-1.25 Write a short Python function that takes a strings, representing
a sentence, and returns a copy of the string with all punctuation removed.
For example, if given the string"Lets try, Mike.",
this function would return"Lets try Mike"."""

import re

def remove_nonlitter(s):
    s = re.sub(r"\W+", ' ', s)
    return s

if __name__ == '__main__':
    print("Lets try, Mike.")
    print(remove_nonlitter("Lets try, Mike."))
    print('-------')
