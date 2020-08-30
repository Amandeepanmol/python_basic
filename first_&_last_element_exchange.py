Pro1=>Program to interchange first and last elements in a list
eg; list1=[12,35,9,56,24]
    list1=[24,35,9,56,12]
   
list1=[89,78,67,99,95]                        #list creation
length=len(list1)                             #we find the length of list
temp=list1[0]                                 #swapping of first and last index
list1[0]=list1[length-1]
list1[length-1]=temp
print(list1)

    
2 Method:
----------

list1=[89,78,67,99,95]   
f=list1.pop(0)           # taken out the first element and stored in f
l=list1.pop(-1)          # taken out the last element and stored in l

list1.insert(0,l)        # insert the last element at the 0 index using insert
list1.append(f)          # same way appended the first element at last index
print(list1)             # this way first and last element is interchanged

