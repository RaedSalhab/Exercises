"""
    R-5.1 Execute the experiment from Code Fragment 5.1 and compare the results
on your system to those we report in Code Fragment 5.2.
"""

import sys
data = []
n = 27
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Lingth: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)

#Code Results
"""
Lingth:   0; Size in bytes:   56
Lingth:   1; Size in bytes:   88
Lingth:   2; Size in bytes:   88
Lingth:   3; Size in bytes:   88
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
# In all my results small than fragment code 5.2 by 16 bytes
