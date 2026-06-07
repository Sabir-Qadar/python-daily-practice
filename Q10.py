''' Write a Python program to print all the two digit numbers that 
are divisible by either 3 or 7. Use a for loop and the range function'''

for i in range(10,100):
    if i %3 ==0 or i % 7==0:
        print(i)
        