'remove vowels from a string'
s=input("enter any string : ")
s1=""

for i in s:
    if i in 'aeiouAEIOU':
        pass
    else:
        s1=s1+i
print("strings after removing vowels :",s1)