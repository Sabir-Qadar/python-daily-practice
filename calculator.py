import sys
print("""Please select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
""")

choice=int(input("select operation 1,2 or3"))

if choice not in (1,2,3):
    print("invalid choice")
    sys.exit()

a=int(input("enter first number"))
b=int(input("enter second number"))

if choice == 1:
        result=a+b

elif choice ==2:
        result=a-b

else:
        result=a*b
    
print("the result is : ", result)
