"""C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]."""

def create_list(n):
    result = []
    for i in range(n):
        result.append(i * (i + 1))

    return result

if __name__ == "__main__":
    print(create_list(10))
