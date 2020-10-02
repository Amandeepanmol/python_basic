import random                 #random module is imported
x=random.random()      #it generates the float no between 0.0 to 1.0
print(x)

x=random.randint(1,100)       #it generates the random no between specified integers
print(x)

x=random.randrange(1,100,5) #it generats random no between given ranges
print(x)

l1=[78,89,88,98]        #it randomly reorders the elements in a list
random.shuffle(l1)
print(l1)

--------------------------------------
Eg:
  
 Write a program to generate three numbers and check if all the numbers are same then print “1st prize”, if two are same then print “2nd prize” else print”3rd prize”.

Code:
-------

import random
num1 = random.randrange(1,100)
num2 = random.randrange(1,100)
num3 = random.randrange(1,100)
if num1 == num2 and num1 == num3:
    print("1st Prize")
elif num1==num2 or num2==num3 or num1==num3:
    print("2nd Prize")
else:
    print("Try Again!")	
