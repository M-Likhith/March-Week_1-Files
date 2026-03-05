Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Identify Operators
a=7
if type(a) is int:
    print ("it is int")

    
it is int
if type(a) is float:
    print("it is int")

    
if type(a) is not float:
    print("it is int")

    
it is int

#Membership Operators
a=2,4,3,5,6,7,8,9
if 8 in a:
    print("8 is in a")

    
8 is in a
if 11 in  a:
    print("11 is in a")

    
if 12 not in a:
    print("12 is not in a ")

    
12 is not in a 

#Bitwise Operators
a=3
>>> b=5
>>> a&b
1
>>> bin(2)
'0b10'
>>> bin(3)
'0b11'
>>> bin(5)
'0b101'
>>> a|b
7
>>> a=2
>>> b=8
>>> a|b
10
>>>  a=7
...  
SyntaxError: unexpected indent
>>> a=7
>>> ~a
-8
>>> a=3
>>> b=6
>>> a^b
5
>>> a=3
>>> a<<2
12
>>> bin(3)
'0b11'
>>> a=5
>>> a<<3
40
>>> bin(4)
'0b100'
>>> a>>2
1
>>> a>>3
0
