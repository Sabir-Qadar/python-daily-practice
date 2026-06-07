''' Develop a Python program to perform division of two user-input numbers using exception 
handling. Analyze how the 'try', 'except', and 'finally' blocks manage errors like division by 
zero'''

# Function to perform division with exception handling
def divide_numbers():
    try:
        num1 = float(input("enter first number "))
        num2 = float(input("enter second number "))

        result =num1/num2
        print("result of division is :", result)

    except ZeroDivisionError:
        print("error: division by zero is not allowed.")

    except ValueError:
        print("error: please enter valid numbers.")

    finally:
        print("execution completed.")

divide_numbers()