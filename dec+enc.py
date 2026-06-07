n=int(input("choose 1 for decrypting message and 2 for encrypting message"))
if n==1:
    s=input("enter any string :")
    k=3
    s1=""
    for i in range (0,len(s)):
      s1=s1+chr(ord(s[i])-k)
    print("decrypted message is :",s1)

elif n==2:
    s=input("enter any string : ")
    k=3
    s1=""
    for i in range(0,len(s)):
      s1=s1+chr(ord(s[i])+k)
    print("encrypted message is :",s1)

else:
   print("invalid input")