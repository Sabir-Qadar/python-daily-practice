'''Develop a Python program using a 'for' loop to demonstrate the use of 'break', 'continue', and 
'pass' statements. Analyze how each statement affects the program’s flow'''

#Demonatrtion of 'break', 'continue', and 'pass' statements in a 'for' loop

print("break example:")
for i in range(1,6):
    if i == 4:
        break # Exit the loop when i is 4                                   
    print(i)    

print("\ncontinue example :")
for i  in range(1,8):
    if i == 3:
        continue # Skip the rest of the loop when i is 3
    print(i)

print("\n pass example : ")
for i in range(1,6):
    if i == 2:
        pass # Do nothing when i is 2
    print(i)