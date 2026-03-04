Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Datatype Conversions
#int
#"int only converts int,float,boolean"
int(8)
8
int(7.62)
7
int("hello")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
int(6+3j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(6+3j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(False)
0

#float , "it only converts int,float,boolean"
float(77)
77.0
float(8.72)
8.72
float("hi")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
float(3+2j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(3+2j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
>>> 
>>> #string , it converts every data type
>>> str(77)
'77'
>>> str(6.92)
'6.92'
>>> str("likhith")
'likhith'
>>> str(8+1j)
'(8+1j)'
>>> str(True)
'True'
>>> 
>>> #complex , it converts everything except string datatype
>>> complex(56)
(56+0j)
>>> complex(4.23)
(4.23+0j)
>>> complex("M")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    complex("M")
ValueError: complex() arg is a malformed string
>>> complex(7+1j)
(7+1j)
>>> complex(False)
0j
>>> 
>>> #Boolean , it tells true for datatype
>>> bool(76)
True
>>> bool(1.23)
True
>>> bool("L")
True
>>> bool(2+9j)
True
>>> bool(True)
True
