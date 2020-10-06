import array as arr
#n=int(input())                              #1
arr=arr.array('i',[])
n=int(input())

for i in range(n):
    ele=int(input("Enter elements: "))
    arr.append(ele)
print(arr)
-----------------------

ind=int(input("Enter index u want to delete: "))
arr.pop(ind)                 #2
print(arr)
-------------------------

val=int(input("ENter the value to be searched: "))
for i in arr:
    if i==val:
        if(val%2==0):            #3
            print("even and preseant at",arr.index(val))
        else:
            print("odd and preseant at",arr.index(val))

print("Reversed array.....")
arr.reverse()               #4
print(arr)

-------------------------

'''
import array as arr
a=arr.array('i',[1,9,8,5,2,3,2,2,2,3,2,0])
print(a)                             #5
c=0
b=int(input("enter value to be searched:"))
for i in a:
    if i==b:
        c=c+1
print(c)
'''
---------------------------------------
'''
import array as arr
a=arr.array('i',[0,9,8,5,3,2,3,4,2])
print(a)                               #6

ele=int(input("enter value to be removed:"))
if ele in a:
    a.remove(ele)
print(a)

'''
