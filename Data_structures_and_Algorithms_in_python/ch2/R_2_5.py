"""R-2.5 Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter."""

class CreditCard:
    
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if not isinstance(price,(int,float)):
            raise TypeError('price must be numeric')

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        if not isinstance(amount,(int,float)):
            raise TypeError('amount must be numeric')
        self._balance -= amount


if __name__ == '__main__':
    user = CreditCard('raed', 'aib', '2344 4444 5566 7777', 1000)
    print(user.charge(500))
    print(user.get_balance())
    print(user.charge(300.0))
    print(user.get_balance())
    print(user.charge(400))
    print(user.get_balance())
    user.make_payment(100)
    print(user.get_balance())
    user.make_payment('100')