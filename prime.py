def is_prime(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def printPFactors(n):
    for i in range(2, n + 1):
        if is_prime(i):
            while n % i == 0:
                print(i)
                n = n // i
            


n=int(input("enter a number : "))
printPFactors(n)

