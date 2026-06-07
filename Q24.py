''' Define a list of integers from 1 to 10. Write a Python program to extract the first five  
elements using list slicing and reverse the list using slicing'''

l1=list(range(1,11))
print("original list :",l1)

first_five=l1[:5]
print("first five elements :", first_five)

reversed_list=l1[::-1]
print("reverseed list :", reversed_list)
