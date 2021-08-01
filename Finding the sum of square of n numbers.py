n = int(input("Enter the n-th number : "))
sum = 0
for s in range(1, n + 1):
    sum = sum + (s * s)
    print("The sum of squares is :", sum)