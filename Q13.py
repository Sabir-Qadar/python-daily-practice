''' Write a Python function to implement pow (x, n)'''
def power(x,n):
     if n==0:
           return 1
     elif n<0:
        return ("enter a positive number")
     else:
        return x * power(x,n-1)
x = float(input("enter base number :"))
n = int(input("enter exponent number : "))
result = power(x,n)
print(f"{x} raised to the power {n}  is :  ")
print(result)

