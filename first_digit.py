def getfirstdigit(x):
    while x>10:
        x=x//10
        return x
x=int(input("enter number : "))
print(getfirstdigit(x))