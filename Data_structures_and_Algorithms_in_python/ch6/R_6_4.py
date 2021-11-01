"""
R-6.4 Give a recursive method for removing all the elements from a stack.
"""

class Empty(Exception):
    pass

class ArratStak:
    """ LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def __str__(self):
        return str(self._data)
    
    def clear(self): # Solution is here
        self.pop()
        if not self.is_empty():
            self.clear()

if __name__ == '__main__':
    S = ArratStak()
    for i in range(10):
        S.push(i)

    print(S)
    S.clear()
    print(S)
