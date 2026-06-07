''' Design a Python program using a for loop and the range () function to calculate and print the 
sum of all even numbers between 1 and 50.'''
sum = 0
for i in range(1,51):
    if i % 2 ==0:
        sum += i
print("sum of all even numbers are : ", sum)
