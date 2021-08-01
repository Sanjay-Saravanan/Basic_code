import decimal

Num1 = float(input('Num1:'))
Num2 = float(input('Num2:'))
Mul = decimal.Decimal(Num1) * decimal.Decimal(Num2)
print(f'The product of {Num1} is {Num2} is %0.4f' % Mul)
