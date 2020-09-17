def selectionsort(l1):
    for i in range(0,len(l1)-1):
        min_val=min(l1[i:])              #min() will give ous the smallest no
        min_ind=l1.index(min_val,i)      #index() will give ous the index of smallest number
        l1[i],l1[min_ind]=l1[min_ind],l1[i]    #swapping done 


l1=[98,88,99,0,76,78,0]
selectionsort(l1)
print(l1)
