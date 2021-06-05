"""P-1.32 Write a Python program that can simulate a simple calculator,
using the console as the exclusive input and output device. That is, each
input to thecalculator, be it a number, like 12.34 or 1034, or an operator,
like + or =, can be done on a separate line.  After each such input, you should
output to the Python console what would be displayed on your calculator."""

def simple_calculator():
    result = 0
    input_list = []
    operator = ['+', '-', '*', '/']

    try:
        while True:
            item = input('_> ')
            if item in ['', '=']:
                raise EOFError
            elif item in operator:
                input_list.append(item)
            elif isinstance(float(item), float):
                input_list.append(float(item))

    except (EOFError , ValueError):
        pass

    if input_list[0] in operator:
        input_list.remove(input_list[0])

    while '*' in input_list:
        i = input_list.index('*')
        input_list[i-1] *= input_list[i+1]
        del input_list[i:i+2]

    while '/' in input_list:
        i = input_list.index('/')
        input_list[i-1] /= input_list[i+1]
        del input_list[i:i+2]

    while '+' in input_list:
        i = input_list.index('+')
        input_list[i-1] += input_list[i+1]
        del input_list[i:i+2]

    while '-' in input_list:
        i = input_list.index('-')
        input_list[i-1] -= input_list[i+1]
        del input_list[i:i+2]

    result = input_list[0]

    print('=> ' + str(result))

if __name__ == '__main__':
    simple_calculator()
