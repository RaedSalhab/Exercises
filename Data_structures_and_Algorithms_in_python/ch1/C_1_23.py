"""C-1.23 Give an example of a Python code fragment that attempts to write
an element to a list based on an index that may be out of bounds.
If that indexis out of bounds, the program should catch the exception
that results, andprint the following error message:“Don’t try buffer
overflow attacks in Python!”"""

def fragment_item(sentence, item_index):
    a_list = sentence.split()
    if item_index >= len(a_list):
        raise IndexError("Don’t try buffer overflow attacks in Python!")
    item = a_list[item_index]

    return item


if __name__ == '__main__':
    x = 'Give an example of a Python code fragment that attempts to write \
    an element to a list based on an index that may be out of bounds'
    print(fragment_item(x, 2))
    print(fragment_item(x, 150))
