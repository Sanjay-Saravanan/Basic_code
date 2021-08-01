import decimal

Num1 = float(input('Num1 :'))
Num2 = float(input('Num2 :'))
Division = decimal.Decimal(Num1) / decimal.Decimal(Num2)
print(f'The quotient of {Num1} / {Num2} is %0.4f' % Division)