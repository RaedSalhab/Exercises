"""C-1.21 Write a Python program that repeatedly reads lines from standard
input until an EOFError is raised, and then outputs those lines in reverse
order (a user can indicate end of input by typing ctrl-D)."""

def input_list():
    result = []
    try:
        while True:
            item = input('>>>> ')
            if item == '':
                raise EOFError
            result.append(item)
    except EOFError:
        pass

    result.reverse()
    return result

if __name__ == '__main__':
    print(input_list())
