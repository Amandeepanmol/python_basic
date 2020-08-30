Prog2: Program to swap two elements in a list
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

l1=[98,89,90,86,96]
pos1=int(input())
pos2=int(input())
l1[pos1],l1[pos2]=l1[pos2],l1[pos1]
print(l1)

2nd Method:
------------
l1=[98,89,90,86,96]
pos1=int(input())
pos2=int(input())
temp=l1[pos1]
l1[pos1]=l1[pos2]
l1[pos2]=temp
print(l1)
