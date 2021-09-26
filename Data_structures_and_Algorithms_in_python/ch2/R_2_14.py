"""R-2.14 Implement the mul method for the Vector class of Section 2.3.3, so
that the expression u v returns a scalar that represents the dot product of
the vectors, that is, ∑ di=1 u i · v i ."""

from ast import While
from unittest import result


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self ,d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other): # Add Methode __radd__ to solution exercise
        """Return sum of two vectors"""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        """Return difrence between two vectors"""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        """Return negative value for vector"""
        
        for j in range(len(self)):
            self[j] = -1 * self[j]
        return self

    def __eq__(self,other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector diﬀers from other."""
        return not self == other

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'

    
    def __mul__(self, number):
        """Return result multiplication victor with intger number"""
        if isinstance(number, int) and number >= 1:
            result = Vector(len(self) * number)
            for i in range(len(result)):
                result[i] = self[i % len(self)]

        else:
            raise TypeError('Number must be positive intger')

        return result
    
    # Solution here
    def __mul__(self, other):
        """Return result dot produt bitween two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        i = 0
        result = 0
        while i < len(self):
            result += self[i] * other[i]
            i += 1
        return result


    def __rmul__(self, number):
        """Return result multiplication victor with intger number"""
        if isinstance(number, int) and number >= 1:
            result = Vector(len(self) * number)
            for i in range(len(result)):
                result[i] = self[i % len(self)]

        else:
            raise TypeError('Number must be positive intger')

        return result

if __name__ == '__main__':
    u = Vector(5)
    l = [5, 3, 10, -2, 1]
    for i in range(len(u)):
        u[i] = l[i]
    v = Vector(5)
    l = [6, 2, 8, 9, 9]
    for i in range(len(v)):
        v[i] = l[i]
    print(u , v)
    x = u * v
    print(x)
