'''enter two strings and compare both the strings if both are equal then copy the 
first string  to third string  otherwise concatenate both the stirng to third string
and display all the string along with their lengths
'''
s1=input("enter first string : ")
s2=input("enter second string : ")
if s1==s2:
    s3=s1
else:
    s3=s1+s2

print("first string is : ", s1,len(s1))
print("second string is : ",s2,len(s2))
print("third string is : ",s3,len(s3))
