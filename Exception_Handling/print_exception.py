Code:
------
try:
    a=int(input())
    b=int(input())
    print(a/b)
except Exception as e:
    print(type(e))               #type of exception
    print(e.__class__)           #type of exception
    print(e.__class__.__name__)  #exception name only
    print(e)                     #description of exception
-------------------------------------------------------------------
Output:
-------
When
RESTART: C:/Users/hp/AppData/Local/Programs/Python/Python37-32/28 sept.py =
a=10
b=2
5.0

When
RESTART: C:/Users/hp/AppData/Local/Programs/Python/Python37-32/28 sept.py =
10
0
<class 'ZeroDivisionError'>
<class 'ZeroDivisionError'>
ZeroDivisionError
division by zero

When
RESTART: C:/Users/hp/AppData/Local/Programs/Python/Python37-32/28 sept.py =
a=10
b=a
<class 'ValueError'>
<class 'ValueError'>
ValueError
invalid literal for int() with base 10: 'a'

