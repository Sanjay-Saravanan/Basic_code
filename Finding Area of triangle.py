# Finding area of triangle using Heron's formula
A = float(input('Side A:'))
B = float(input('Side B:'))
C = float(input('Side C:'))
s = (A + B + C) / 2
Area = (s * (s - A) * (s - B) * (s - C)) ** 0.5
print('The area of the triangle is %0.2f' % Area)
