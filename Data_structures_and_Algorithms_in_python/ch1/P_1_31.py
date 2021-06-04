"""P-1.31 Write a Python program that can “make change.”  Your program
should take two numbers as input, one that is a monetary amount charged and
the other that is a monetary amount given.  It should then return the number
of each  kind  of bill  and  coin  to give back  as change  for the  difference
between the amount given and the amount charged.  The values assigned to the
bills and coins can be based on the monetary system of any currentor former
government.  Try to design your program so that it returns asfew bills and
coins as possible."""

def refund(charged, given):
    # the monetary system for jordan (JOD)
    bills_coins = {50.00: 0, 20.00: 0, 10.00: 0, 5.00: 0, 1.00: 0, 0.50: 0,
    0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
    try:
        remaining = charged - given
        if remaining > 0:
            for money_class in bills_coins.keys():
                bills_coins[money_class] = remaining // money_class
                remaining -= (bills_coins[money_class] * money_class)
                bills_coins[money_class] = int(bills_coins[money_class])
    except TypeError:
        print('charged and given must be numbers')
    return bills_coins

if __name__ == "__main__":
    print(refund(100, 23))
    print(refund(150, 50))
    print(refund(1000, 246))
    print(refund("1200", 48))
