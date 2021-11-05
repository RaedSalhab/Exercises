"""

    A friend of mine takes the sequence of all numbers from 1 to n (where n > 0).
    Within that sequence, he chooses two numbers, a and b.
    He says that the product of a and b should be equal to the sum of all numbers in the sequence, 
    excluding a and b.
    Given a number n, could you tell me the numbers he excluded from the sequence?

The function takes the parameter: n (n is always strictly greater than 0) and returns an array 
or a string (depending on the language) of the form:

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]

with all (a, b) which are the possible removed numbers in the sequence 1 to n.

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ... will be sorted in increasing order of the "a".

It happens that there are several possible (a, b). The function returns an empty array (or an 
empty string) if no possible numbers are found which will prove that my friend has not told the truth! (Go: in this case return nil).
Examples:

removNb(26) should return [(15, 21), (21, 15)]
or
removNb(26) should return { {15, 21}, {21, 15} }
or
removeNb(26) should return [[15, 21], [21, 15]]
or
removNb(26) should return [ {15, 21}, {21, 15} ]
or
removNb(26) should return "15 21, 21 15"

or

in C:
removNb(26) should return  {{15, 21}{21, 15}} tested by way of strings.
Function removNb should return a pointer to an allocated array of Pair pointers, 
each one also allocated. 

Note

See examples of returns for each language in "RUN SAMPLE TESTS"

"""

from time import time_ns

def remov_nb1(n):
    lst = []
    for i in range(n+1):
        for j in range(n+1):
            if i != j:
                if (i * j) == (sum(range(n+1))- i - j):
                    lst.append((i, j))
    return lst

def remov_nb(n):
    start = time_ns()
    lst = []
    sum_value = sum(range(n+1))
    for i in range(n//2, n+1):
        j = (sum_value - i) / (i + 1)
        if j in range(n//2, n+1):
            lst.append((i ,j))

    end = time_ns()
    print ((end - start)/1000000)
    return lst

print(remov_nb(26))
print(remov_nb(100))
print(remov_nb(101))
print(remov_nb(100000))

# need long time to fine solution
