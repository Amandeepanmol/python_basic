Prog 4:Program to remove Nth occurrence of the given word


l1=['hii','bye','hii','hello','hii']
l=[]
wrd=input("Enter the word")
n=int(input())
c=0
for i in l1:
    if i==wrd:
        c+=1
        if c!=n:
            l.append(i)
    else:
        l.append(i)
l1=l
print(l1)
