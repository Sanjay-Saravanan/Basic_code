import decimal

Num1 = float(input('Num1:'))
Num2 = float(input('Num2:'))
Add = decimal.Decimal(Num1) + decimal.Decimal(Num2)
print(f'The Addition of {Num1} and {Num2} is %0.4f' % Add)
