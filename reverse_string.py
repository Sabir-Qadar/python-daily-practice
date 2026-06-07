s=input("enter any string : ")
s1=""

for i in range (len(s)-1,-1,-1):
    s1=s1+s[i]
    s1=s1.lstrip()
    
print("reversed string is : ",s1)