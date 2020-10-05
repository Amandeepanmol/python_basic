Ist Method:
------------

n=int(input())
dict1={}
for i in range(n):
    key=int(input("Enter key: "))
    value=input("Enter value: ")
    dict1[key]=value
print(dict1)
sumofkey=0
for i in dict1:
    sumofkey+=i
print("Sum of keys in dictionary is :",sumofkey)
-----------------------------------------------------------------
IInd Method:
--------------

n=int(input())
dict1={}
for i in range(n):
    key=int(input("Enter key: "))
    value=input("Enter value: ")
    dict1[key]=value
print(dict1)
x=0
x=sum(dict1.keys())
print(x)
-----------------------------------------------------------------------

OUTPUT:
-------

>>> 
== RESTART: C:/Users/hp/AppData/Local/Programs/Python/Python37-32/5 oct.py ==
3
Enter key: 1
Enter value: a
Enter key: 5
Enter value: b
Enter key: 3
Enter value: c
{1: 'a', 5: 'b', 3: 'c'}
9
