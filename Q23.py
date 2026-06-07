'''Write a Python program to take a string input from the user and perform the following: 
(i)Convert the string to uppercase. (ii)Count the number of vowels in the string.'''

def upper_case(s1):
    return s1.upper()

def count_vowels(s1):
    count = 0
    for char in s1:
        if char in 'aeiouAEIOU':
            count += 1
    return count
        
def main():
    s1 = input("enter a string: ")
    print("string in uppercase : ", upper_case(s1))
    print("total numbers of vowels in string : ", count_vowels(s1))

main()