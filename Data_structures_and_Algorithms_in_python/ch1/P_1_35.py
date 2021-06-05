"""P-1.35 The birthday paradox says that the probability that two people in
a room will have the same birthday is more than half, provided n, the number
of people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test this
paradox by a series of experiments on randomly generated birthdays, which test
this paradox for n=5,10,15,20,...,100."""
import random

def is_same_birthday(n):
    same_birthday = 0
    birthdays = []
    while n >= 1:
        birthdays.append(random.randint(1, 365))
        n -= 1
    for day in birthdays:
        x = birthdays.count(day)
        if x >= 2:
            same_birthday = 1

    return same_birthday

def birthday_paradox():
    results = {}
    probability = 0
    sum = 0
    for n in range(5, 105, 5):
        key = n
        value = is_same_birthday(n)
        results.update({key: value})
        sum += value

    probability = sum /len(results.values())
    return probability

if __name__ == '__main__':
    print('The probability =', str(birthday_paradox()), 'is more than 0.5.')
