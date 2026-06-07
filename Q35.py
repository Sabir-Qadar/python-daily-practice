''' Design a Python program that performs the following operations on a user-defined string: 
(i)Check if the string is a palindrome (reads the same backward as forward). (ii)Replace all 
vowels in the string with the character '#'.Use appropriate comment for increasing the 
readability of the program'''

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for accurate comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]
# Function to replace all vowels in the string with '#'
def replace_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char in vowels :
            result += '#'
        else:
            result += char 

    return result 
# Input from the user
user_string =input("enter a string :")
# Check if the string is a palindrome
if is_palindrome(user_string):
    print(f'"{user_string}" is a palindrome')
else:
    print(f'"{user_string}" is not a palindrome')
# Replace vowels in the string
modified_string = replace_vowels(user_string)
print("String after replacing vowels with '#':", modified_string)
