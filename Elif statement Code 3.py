num = int(input('Enter an Number :'))
if num >= 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is prime")

        else:
            print(f'{num} is not prime')


