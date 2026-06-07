#decrypt the message
s=input("enter any string :")
k=3
s1=""
for i in range (0,len(s)):
    s1=s1+chr(ord(s[i])-k)
print("decrypted message is :",s1)