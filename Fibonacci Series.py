n_terms: int = int(input("How many terms ?: "))
n1 = 0
n2 = 1
count = 0
if n_terms <= 0:
    print("Please enter a +ve number : ")
elif n_terms == 1:
    print("Fibonacci terms :", n_terms, ":")
    print(n1)
else:
    print("Fibonacci Series is :")
    while count < n_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
