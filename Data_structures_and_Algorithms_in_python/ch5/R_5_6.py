"""
R-5.6 Our implementation of insert for the DynamicArray class, as given in
    Code Fragment 5.5, has the following inefﬁciency. In the case when a re-
    size occurs, the resize operation takes time to copy all the elements from
    an old array to a new array, and then the subsequent loop in the body of
    insert shifts many of those elements. Give an improved implementation
    of the insert method, so that, in the case of a resize, the elements are
    shifted into their ﬁnal position during that operation, thereby avoiding the
    subsequent shifting.
"""

import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if k < 0: # Solution here
            k += self._n
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _resize_shift(self, c, k): # This solution for this exercise
        B = self._make_array(c)
        for i in range(self._n, k, -1):
            B[i] = self._A[i - 1]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize_shift(2 * self._capacity, k)
        else:
            for j in range(self._n, k, -1):
                self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1
