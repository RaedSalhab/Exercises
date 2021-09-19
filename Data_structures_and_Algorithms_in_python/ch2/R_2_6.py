"""R-2.6 If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent."""

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
        elif amount < 0:
            raise ValueError('amount cannot be negative')
        self._balance -= amount


if __name__ == '__main__':
    user = CreditCard('raed', 'aib', '2344 4444 5566 7777', 1000)
    user.charge(20)
    user.make_payment(10)
    print(user.get_balance())
    user.make_payment(-10)