n=int(input("Enter no of items in dictionary:"))
d={}
for i in range(n):
    key=int(input("Enter key: "))
    val=input("Enter value: ")
    d[key]=val
print(d)

print("Enter the key u want to delete: ")
k=int(input("Input the key: "))
del d[k]
print(d)
