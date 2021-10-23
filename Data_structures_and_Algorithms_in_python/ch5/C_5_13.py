"""
C-5.13 In the experiment of Code Fragment 5.1, we begin with an empty list. If
    data were initially constructed with nonempty length, does this affect the
    sequence of values at which the underlying array is expanded? Perform
    your own experiments, and comment on any relationship you see between
    the initial length and the expansion sequence.
"""

import sys
data = [1, 2, 4, 5]
n = 23
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Lingth: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)


# When create nonempty array take memory space enoph for array length,
# if append item use amortize principle   

"""
Lingth:   4; Size in bytes:   88
Lingth:   5; Size in bytes:  120
Lingth:   6; Size in bytes:  120
Lingth:   7; Size in bytes:  120
Lingth:   8; Size in bytes:  120
Lingth:   9; Size in bytes:  184
Lingth:  10; Size in bytes:  184
Lingth:  11; Size in bytes:  184
Lingth:  12; Size in bytes:  184
Lingth:  13; Size in bytes:  184
Lingth:  14; Size in bytes:  184
Lingth:  15; Size in bytes:  184
Lingth:  16; Size in bytes:  184
Lingth:  17; Size in bytes:  256
Lingth:  18; Size in bytes:  256
Lingth:  19; Size in bytes:  256
Lingth:  20; Size in bytes:  256
Lingth:  21; Size in bytes:  256
Lingth:  22; Size in bytes:  256
Lingth:  23; Size in bytes:  256
Lingth:  24; Size in bytes:  256
Lingth:  25; Size in bytes:  256
Lingth:  26; Size in bytes:  336
"""
