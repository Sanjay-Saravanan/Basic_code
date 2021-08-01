Num1 = float(input('Num1:'))
Num2 = float(input('Num2:'))
Num3 = float(input('Num3:'))

if (Num1 <= Num2) and (Num1 <= Num3):
    smallest = Num1
elif (Num2 <= Num1) and (Num2 <= Num3):
    smallest = Num2
else:
    smallest = Num3

print("The smallest number is",  smallest)
