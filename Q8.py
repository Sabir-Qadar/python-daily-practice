'''Write a Python program using a while loop that repeatedly asks the user to enter a number 
and display it. If the user enters a negative number, the program should stop asking and print 
"Loop ended". Use a break statement in your program'''

while True:
    num = float(input("enter number :"))
    if num <0:
        print("loop ended ")
        break
    print("you entered :",num)
