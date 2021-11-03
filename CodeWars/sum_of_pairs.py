"""
Sum of Pairs

Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]

Negative numbers and duplicate numbers can and will appear.

NOTE: There will also be lists tested of lengths upwards of 
10,000,000 elements. Be sure your code doesn't time out.
"""

def sum_pairs(ints, s):
    x = 0
    y = 0
    for i in range(len(ints)):
        if (s - ints[i]) in ints[i+1:]:
            j = ints.index(s - ints[i])
            if j > y :
                x = i
                y = j
    if y == 0:
        return None
    return [ints[x], ints[y]]
    

        
print(sum_pairs([10, 5, 2, 3, 7, 5], 10)) #[3, 7]
print(sum_pairs([4, 5, 2, 8, 7, 5], 12)) #[5, 7]
print(sum_pairs([5, 8, 2, 0, 7, 5], 10)) #[8, 2]
print(sum_pairs([10, 5, 2, 3, -3, 4], 10)) #None