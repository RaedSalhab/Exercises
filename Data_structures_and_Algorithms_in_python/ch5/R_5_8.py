"""
R-5.8 Experimentally evaluate the efﬁciency of the pop method of Python’s list
    class when using varying indices as a parameter, as we did for insert on
    page 205. Report your results akin to Table 5.5.
"""

from time import time_ns

N = [100, 1000, 10000, 100000, 1000000]

def compute_pop(n):
    
    result = []
    for k in [n-1 , n // 2, 0]:
        data  = [None] * n 
        start = time_ns()/1000
        data.pop(k)
        end = time_ns()/1000
        result.append(end - start)
    text = '{0:7.2f}  {1:7.2f}   {2:7.2f}'.format(result[2],result[1], result[0])
    return text

print('            k = 0 | k = n//2 | k = n')
print('            ------+----------+--------')
for n in N:
    print('{0:8d}  '.format(n) + compute_pop(n))
