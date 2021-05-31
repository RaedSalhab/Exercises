"""C-1.19 Demonstrate how to use Python’s list comprehension  syntax to
produce the list[a,b,c, ...,z], but without having to type all 26
suchcharacters literally."""

def litter_list():
    result = []
    for i in range(97, 123):
        result.append(chr(i))

    return result

if __name__ == '__main__':
    print(litter_list())
