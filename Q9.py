''' Write a Python program that displays the greatest among three numbers entered by the user. 
Use an if-elif-else block to display the appropriate message.'''

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))

if num1 > num2 and num1 > num3:
    print("greatest number is :",num1)
elif num2 > num1 and num2 > num3:
    print("greatest number is :",num2)
else:
    print("greatest number is :",num3)