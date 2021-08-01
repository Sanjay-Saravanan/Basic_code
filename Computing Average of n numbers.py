# Calculating average of 'n' numbers
Num = int(input('Enter the total count of numbers: '))
total_sum = 0
for n in range(Num):
    numbers = float(input('Enter number : '))
    total_sum += numbers
Avg = total_sum / Num
print(f'Average of {Num} numbers is {Avg}')
