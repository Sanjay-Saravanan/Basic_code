Num = int(input('Enter a Number:'))
flag = False
if Num > 1:
    for i in range(2, Num):
        if (Num % i) == 0:
            flag = True
            break
if flag:
    print(f"{Num} is not a prime number")
else:
    print(f"{Num} is a prime number")