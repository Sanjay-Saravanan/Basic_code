def multiple(*a):
    a = float(input('Enter Number :').split())
    result = 1
    for i in a:
        result = result * i
    return result


result = float(input('Enter Number :').split())
print(result)
