# Finding area of rectangle
import decimal

A = float(input('Side A:'))
B = float(input('Side B:'))
Area = decimal.Decimal(A) * decimal.Decimal(B)
print(f'The area of rectangle is %0.4f' % Area)
