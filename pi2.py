pi = 22/7
length = input('how many digits of pi would you like? : ')
m = int(length)
print(round(pi,m))

'''
Easiest way to calculate value of pi to nth digit but,
There's a big but it will only calculate upto 15th places
hence we'll use chudnovsky formula 

'''
from math import factorial
from decimal import Decimal , getcontext 

getcontext().prec = 1000
pi = input('how many digits of pi would you like? : ')
n = int(pi)

def cal(n):
    t  = Decimal(0)
    pi = Decimal(0)
    denominator = Decimal(0)

    for k in range(n):
        t           = ((-1)**k)*(factorial(6*k))*(13591409 + 545140134*k)
        denominator = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi         += Decimal(t)/Decimal(denominator)
    
    pi = pi * (Decimal(12)/Decimal(640320 ** Decimal(1.5)))
    pi = 1/pi
    return round(pi,n)
print(cal(n))

