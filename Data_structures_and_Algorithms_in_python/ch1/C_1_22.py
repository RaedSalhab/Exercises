"""C-1.22 Write a short Python program that takes two arraysaandbof length n
storing int values, and returns the dot product of a and b. That is, it
returns an array c of length n such that c[i]=a[i]·b[i],fori=0,...,n−1."""

def dot_product(a , b):
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])

    return c

if __name__ == '__main__':
    print(dot_product([2, 5, 7, 9], [3, 4, 6, 8]))
