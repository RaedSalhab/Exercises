"""P-1.34 A common punishment for school children is to write out a sentence
multiple times.  Write a Python stand-alone  program that will write out the
following  sentence  one  hundred  times:   “I  will  never  spam  my  friends
again.”  Your program should number each of the sentences and it should make
eight different random-looking typos."""

import random

def rewrite():
    sentences = ["I well never spam my friends again.",
        "I wil never spam my friends again.",
        "I will nevr spam my friends again.",
        "I will never sbam my friends again.",
        "I will never spam me frends again.",
        "I will never spam my frinds again.",
        "I will never spam my friends agin.",
        "I will nver spam my friends again.",]

    for num in range(100):
        sentence = random.choice(sentences)
        print(str(num + 1), sentence)


if __name__ == '__main__':
    rewrite()
