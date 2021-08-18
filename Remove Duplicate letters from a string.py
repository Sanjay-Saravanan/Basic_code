def removeDuplicate(str):
    s = set(str)
    s = "".join(str)
    print("Without order", s)
    t = ""
    for i in str:
        if i in t:
            pass
        else:
            t = t + i
            print("Without order", t)


str = input("Enter a String: ")
removeDuplicate(str)
