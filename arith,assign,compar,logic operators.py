Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Operators
#Arithmetic Operators

a=8
b=12
print(a+b)
20
print(a-b)
-4
print(a*b)
96
print(a//b)
0
print(a/b)
0.6666666666666666
print(a**b)
68719476736
print(a%b)
8

#Assignment Operators
a=4
b=8
a+=b
a
12
a-=b
a
4
a*=b
a
32
a//=b
a
4
a/=b
a
0.5
a**=b
a
0.00390625
a%=b
a
0.00390625

b
8
b+=a
b
8.00390625
b-=a
b
8.0
b*=a
b
0.03125
b//=a
b
8.0
b/=a
b
2048.0
b**=a
b
1.030231637686041
b%=a
b
0.0028878876860409797

#Comparison Operators
a=23
b=34
a<b
True
a>b
False
b>a
True
b<a
False
a>=b
False
a<=b
True
a!=b
True
a==b
False

>>> #Logical Operators
>>> #and
>>> a=7
>>> b=10
>>> a>b and b<a
False
>>> a>=b and b<=a
False
>>> a!=b and a==b
False
>>> #or
>>> a<b or b>a
True
>>> a>=b or b<=a
False
>>> a==b or b!=a
True
>>> #not
>>> not True
False
>>> not False
True
>>> 
>>> #Identify Operators
>>> a=5
>>> if type(a) is int:
...     print("it is int")
... 
...     
it is int
>>> if type(a) is float:
...     print("it is int")
... 
...     
>>> if type(a) is not float:
...     print("it is int")
... 
...     
it is int
