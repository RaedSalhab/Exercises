"""P-1.29 Write a Python program that outputs all possible strings formed by
using the characters c,a,t,d,o,and g exactly once."""

import random
import math

def all_strings(chr_list):
    result = []
    num_possibles = math.factorial(len(chr_list))
    while len(result) < num_possibles:
        new_string = ''
        random.shuffle(chr_list)
        for item in chr_list:
            new_string += item

        if new_string not in result:
            result.append(new_string)

    return result

if __name__ == '__main__':

    print(all_strings(['c', 'a', 't', 'd', 'o', 'g']))
    print(len(all_strings(['c', 'a', 't', 'd', 'o', 'g'])))
    
