Daily practices:
-----------------
Input : test_dict = {“Gfg” : 5, “is” : 8, “Best” : 10, “for” : 8, “Geeks” : 9},
updict = {“Geeks” : 10, “Best” : 17}
Output : {‘Gfg’: 5, ‘is’: 8, ‘Best’: 17, ‘for’: 8, ‘Geeks’: 10}
Explanation : “Geeks” and “Best” values updated to 10 and 17.

Code:
------

test_dict={}
n=int(input())
for i in range(n):
    key=input(("ENter key "))
    value=int(input("Enter value "))
    test_dict[key]=value
print(test_dict)

updict={"Geeks" : 10, "Best" : 17}

for i in test_dict:
    if i in updict:
        test_dict[i]=updict[i]
print("Updated dictionary is :",test_dict)

