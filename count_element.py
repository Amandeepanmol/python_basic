l=[]
n=int(input("Enter the size of list"))
for i in range(0,n):
    item=int(input())
    l.append(item)
print("List element are :",l)

ele=int(input("Enter the element for which occurrences is to be counted"))
c=0
for i in l:
    if ele==i:
        c+=1
print('{} is present {} times in list'.format(ele,c))
