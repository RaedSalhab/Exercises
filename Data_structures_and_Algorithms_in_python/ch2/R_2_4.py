from dis import pretty_flags


'''
R-2.4 Write a Python class, Flower, that has three instance variables of type str,
int, and ﬂoat, that respectively represent the name of the ﬂower, its num-
ber of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
'''

class Flower():
    def __init__(self, name, petals_num, price):
        self._name = name
        self._petals_num = petals_num 
        self._price = price

    def set_name(self, name):
        self._name = name

    def set_petals(self, petals_num):
        self._petals_num = petals_num

    def set_price(self, price):
        self._price = price

    def get_name(self):
        return self._name

    def get_petals_num(self):
        return self._petals_num

    def get_price(self):
        return self._price


if __name__ == '__main__':
    my_flower = Flower('Sunflower', 25, 3)
    print(my_flower.get_name())
    print(my_flower.get_petals_num())
    print(my_flower.get_price())
    my_flower.set_petals(30)
    my_flower.set_price(4)
    print(my_flower.get_name())
    print(my_flower.get_petals_num())
    print(my_flower.get_price())