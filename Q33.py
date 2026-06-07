'''  Develop a Python program using different data types (int, float, string) to perform addition,  
multiplication, and string concatenation. Analyze how basic operators (+, , /, //) work with    
different data types'''


#integer operations
a=10
b=3

int_add=a+b
int_mul=a*b 
int_div=a/b
int_floor_div=a//b

#float oprations
x=10.5
y=2.5

float_add=x+y
float_mul=x*y
float_div=x/y
float_floor_div=x//y

#string operations
str1="hello"
str2="world"

str_concat=str1 +" "+ str2
str_repeat=str1 * 3

#output
print("Integer Addition:", int_add)
print("Integer Multiplication:", int_mul)
print("Integer Division:", int_div)
print("Integer Floor Division:", int_floor_div)

print("\nFloat Addition:", float_add)
print("Float Multiplication:", float_mul)
print("Float Division:", float_div)
print("Float Floor Division:", float_floor_div)

print("\nString Concatenation:", str_concat)
print("String Repetition:", str_repeat)