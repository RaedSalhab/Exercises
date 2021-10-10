"""C-4.9 Write a short recursive Python function that ﬁnds the minimum and 
maximum values in a sequence without using any loops."""

def max_two(a, b):
    """Return max value between two values"""
    if a >= b:
        return a
    else:
        return b

def min_two(a, b):
    """Return min value between two values"""
    if a < b:
        return a
    else:
        return b

def max_value(seq):
    """Return the maximum value in a sequence"""
    if len(seq) == 1:
        return seq[0]
    return max_two(seq[len(seq) - 1], max_value(seq[:len(seq)-1]))

def min_value(seq):
    """Return the minimum value in a sequence"""
    if len(seq) == 1:
        return seq[0]
    return min_two(seq[len(seq) - 1], min_value(seq[:len(seq)-1]))

def max_min(seq):
    """Return the minimum and maximum values in a sequence"""
    return (max_value(seq), min_value(seq))



seq1 = [23, 4, 7, 1, 67, 9]
seq2 = "My name is Raed"
print(max_min(seq1))
print(max_min(seq2))