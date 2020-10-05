Python 3.6.9 |Anaconda, Inc.| (default, Jul 30 2019, 14:00:49) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py 
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py 
>>> check_Fermat(1,2,3,4)
No, that doesn't work.
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py 
>>> check_Fermat(1,2,3,1.5)
Well that's not what the theorem was claiming...
>>> check_Fermat(1,2,3,9)
No, that doesn't work.
>>> check_Fermat(1.2,3,7.2,2.00001)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    check_Fermat(1.2,3,7.2,2.00001)
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py", line 3, in check_Fermat
    if n>2 and a^n+b^n==c^n:
TypeError: unsupported operand type(s) for ^: 'float' and 'float'
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py 
>>> check_Fermat(1.2,3,7.2,2.00001)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    check_Fermat(1.2,3,7.2,2.00001)
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py", line 4, in check_Fermat
    if n>2 and a^n+b^n==c^n:
TypeError: unsupported operand type(s) for ^: 'float' and 'float'
>>> check_Fermat(1.2,2,3,4)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    check_Fermat(1.2,2,3,4)
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py", line 4, in check_Fermat
    if n>2 and a^n+b^n==c^n:
TypeError: unsupported operand type(s) for ^: 'float' and 'int'
>>> check_Fermat(1,2,3,4)
No, that doesn't work.
>>> check_Fermat(1,2,3,1.000002)
Well that's not what the theorem was claiming...
>>> check_Fermat(1,2,3,2.00001)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    check_Fermat(1,2,3,2.00001)
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py", line 4, in check_Fermat
    if n>2 and a^n+b^n==c^n:
TypeError: unsupported operand type(s) for ^: 'int' and 'float'
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py 
>>> check_Fermat(1,2,3,2.001)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    check_Fermat(1,2,3,2.001)
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py", line 3, in check_Fermat
    if n>2 and float(a^n+b^n==c^n):
TypeError: unsupported operand type(s) for ^: 'int' and 'float'
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py 
>>> check_Fermat(1,2,3,2.0001)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    check_Fermat(1,2,3,2.0001)
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py", line 7, in check_Fermat
    if var_n>2 and var_a^var_n+var_b^var_n==var_c^var_n:
TypeError: unsupported operand type(s) for ^: 'float' and 'float'
>>> check_Fermat(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    check_Fermat(1,2,3,4)
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py", line 7, in check_Fermat
    if var_n>2 and var_a^var_n+var_b^var_n==var_c^var_n:
TypeError: unsupported operand type(s) for ^: 'float' and 'float'
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py 
>>> check_Fermat(1,2,3,4)
You entered something that does not make sense
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py 
>>> check_Fermat(1,2,3,4)
You entered something that does not make sense
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py 
>>> check_Fermat(1,2,3,4)
You entered something that does not make sense
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py 
>>> check_Fermat(1,2,3,4)
You entered something that does not make sense
>>> check_Fermat(1,2,3,2)
Well that's not what the theorem was claiming...
>>> 
KeyboardInterrupt
check_Fermat(1,2,3,4)
>>> check_Fermat(1,2,3,1)
Well that's not what the theorem was claiming...
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py 
>>> 
>>> check_Fermat(1,2,3,4)
No, that doesn't work.
>>> check_Fermat(1,2,3,1)
Well that's not what the theorem was claiming...
>>> check_Fermat(1,2,3,3)
No, that doesn't work.
>>> check_Fermat(1,2,3,2.1)
No, that doesn't work.
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2.py 
>>> check_Fermat(1,2,3,4)
No, that doesn't work.
>>> heck_Fermat(1,2,3,1)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    heck_Fermat(1,2,3,1)
NameError: name 'heck_Fermat' is not defined
>>> check_Fermat(1,2,3,2)
Well that's not what the theorem was claiming...
>>> check_Fermat(1,2,3,1)
Well that's not what the theorem was claiming...
>>> check_Fermat(1,2,3,banana)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    check_Fermat(1,2,3,banana)
NameError: name 'banana' is not defined
>>> check_Fermat(1,2,3,2.1)
You entered something that does not make sense. Make sure all attributes of function are integers.
>>> check_Fermat(1,2,3,'banana')
You entered something that does not make sense. Make sure all attributes of function are integers.
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat
<function check_Fermat at 0x000001F87928F048>
>>> check_Fermat()
Enter a value for "a":1
You entered something that does not make sense. Make sure all attributes of function are integers.
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
You entered something that does not make sense. Make sure all attributes of function are integers.
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat
<function check_Fermat at 0x000002001120F048>
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
No, that doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":1
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":0.5
Enter a value for "b":`
Enter a value for "c":1
Enter a value for "n":2.2
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 12, in check_Fermat
    if int(n)>2 and (int(a)**int(n))+(int(b)**int(n))==(int(c)**int(n)): #Being unnecessarily generous to convert decimal inputs to integers...
ValueError: invalid literal for int() with base 10: '2.2'
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":2.2
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 12, in check_Fermat
    if int(n)>2 and (int(a)**int(n))+(int(b)**int(n))==(int(c)**int(n)): #Being unnecessarily generous to convert decimal inputs to integers...
ValueError: invalid literal for int() with base 10: '2.2'
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 12, in check_Fermat
    if int(n)>2 and (int(a)**int(n))+(int(b)**int(n))==(int(c)**int(n)): #Being unnecessarily generous to convert decimal inputs to integers...
ValueError: invalid literal for int() with base 10: ''
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 5, in check_Fermat
    a=input(int(prompt)) #Being unnecessarily generous to convert decimal inputs to integers...
ValueError: invalid literal for int() with base 10: 'Enter a value for "a":'
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
No, that doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":0.5
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 5, in check_Fermat
    a=int(input(prompt)) #Being unnecessarily generous to convert decimal inputs to integers...
ValueError: invalid literal for int() with base 10: '0.5'
>>> 2
2
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":2.2
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 6, in check_Fermat
    int_a = int(a) #Being unnecessarily generous to convert decimal inputs to integers...
ValueError: invalid literal for int() with base 10: '2.2'
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 13, in check_Fermat
    if int_n>2 and (int_a**int_n)+(int_b**int_b)==(int_c**int_n):
NameError: name 'int_n' is not defined
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
No, that doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":1
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":0.5
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 6, in check_Fermat
    int_a = int(a) #Being unnecessarily generous to convert decimal inputs to integers...
ValueError: invalid literal for int() with base 10: '0.5'
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":2.1
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 6, in check_Fermat
    int_a = int(a) #Being unnecessarily generous to convert decimal inputs to integers...
ValueError: invalid literal for int() with base 10: '2.1'
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
No, that doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":1
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":0.5
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":2.9,1
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 5, in check_Fermat
    a=float(input(prompt)) #Make sure the prompt will accept floating decimals
ValueError: could not convert string to float: '2.9,1'
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":2.9
Enter a value for "b":1
Enter a value for "c":3
Enter a value for "n":5
No, that doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":2.9
Enter a value for "b":1
Enter a value for "c":2
Enter a value for "n":1
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":test
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 5, in check_Fermat
    a=float(input(prompt)) #Make sure the prompt will accept floating decimals
ValueError: could not convert string to float: 'test'
>>> 2
2
3
>>> 
>>> 4
4
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 5, in check_Fermat
    if isinstance(prompt, string):
NameError: name 'string' is not defined
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 5, in check_Fermat
    if isinstance(prompt, string):
NameError: name 'string' is not defined
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":2
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 11, in check_Fermat
    if isinstance(prompt, string):
NameError: name 'string' is not defined
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 7, in check_Fermat
    elif isinstance(promt, float):
NameError: name 'promt' is not defined
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
You need to input only numbers if you want to check if this works...
You need to input only numbers if you want to check if this works...
You need to input only numbers if you want to check if this works...
You need to input only numbers if you want to check if this works...
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 36, in check_Fermat
    if int_n>2 and (int_a**int_n)+(int_b**int_b)==(int_c**int_n):
UnboundLocalError: local variable 'int_n' referenced before assignment
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermar()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    check_Fermar()
NameError: name 'check_Fermar' is not defined
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
You need to input only numbers if you want to check if this works...
You need to input only numbers if you want to check if this works...
You need to input only numbers if you want to check if this works...
You need to input only numbers if you want to check if this works...
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 36, in check_Fermat
    if int_n>2 and (int_a**int_n)+(int_b**int_b)==(int_c**int_n):
UnboundLocalError: local variable 'int_n' referenced before assignment
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
You need to input only numbers if you want to check if this works...
You need to input only numbers if you want to check if this works...
You need to input only numbers if you want to check if this works...
You need to input only numbers if you want to check if this works...
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
You need to input only numbers if you want to check if this works...
You need to input only numbers if you want to check if this works...
You need to input only numbers if you want to check if this works...
You need to input only numbers if you want to check if this works...
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
 
>>> 
>>> test
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    test
NameError: name 'test' is not defined
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
You need to input only numbers if you want to check if this works...
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
You need to input only numbers if you want to check if this works...
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> check_Fermar()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    check_Fermar()
NameError: name 'check_Fermar' is not defined
>>> check_Fermar()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    check_Fermar()
NameError: name 'check_Fermar' is not defined
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
>>> a
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> prompt
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    prompt
NameError: name 'prompt' is not defined
>>> print(prompt)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print(prompt)
NameError: name 'prompt' is not defined
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":a
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py", line 4, in check_Fermat
    a=float(input('Enter a value for "a":'))
ValueError: could not convert string to float: 'a'
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
1.0
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
1
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1.2
1
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":a
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py", line 4, in check_Fermat
    a=float(input('Enter a value for "a":'))
ValueError: could not convert string to float: 'a'
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
You need to input only numbers if you want to check if this works...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1.1
You need to input only numbers if you want to check if this works...
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
1
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1.3
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1.3
1.3
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1.3
You need to input only numbers if you want to check if this works...
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1.3
1.3
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
1
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1.3
1
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":T
You need to input only numbers if you want to check if this works...
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/debut_file5_2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":test
You need to input only numbers if you want this to work...
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
1
Enter a value for "b":2.`
You need to input only numbers if you want this to work...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
1
Enter a value for "b":2.1
2
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
a= 1
Enter a value for "b":2
b= 2
Enter a value for "c":3
c= 3
Enter a value for "n":4
n= 4
No, that doesn't work.
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":2
a= 2
Enter a value for "b":3
b= 3
Enter a value for "c":4
c= 4
Enter a value for "n":1
n= 1
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":a
You need to input only numbers if you want this to work...
Enter a value for "b":1
b= 1
Enter a value for "c":2
c= 2
Enter a value for "n":3
n= 3
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 62, in check_Fermat
    theorem_test(int_a,int_b,int_c,int_n)
UnboundLocalError: local variable 'int_a' referenced before assignment
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":0.5
a= 0
Enter a value for "b":1
b= 1
Enter a value for "c":2
c= 2
Enter a value for "n":2
n= 2
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":0.5
a= 0
Enter a value for "b":2
b= 2
Enter a value for "c":3
c= 3
Enter a value for "n":5.1
n= 5
Sorry, that combination doesn't work.
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
a= 1
Enter a value for "b":2
b= 2
Enter a value for "c":3
c= 3
Enter a value for "n":4
n= 4
Sorry, that combination doesn't work.
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
Sorry, that combination doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":2.1
Enter a value for "b":2
Enter a value for "c":2
Enter a value for "n":2
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":2.1
Enter a value for "b":2.2
Enter a value for "c":2.3
Enter a value for "n":2.4
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":a
You need to input only numbers if you want this to work...
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 62, in check_Fermat
    theorem_test(int_a,int_b,int_c,int_n)
UnboundLocalError: local variable 'int_n' referenced before assignment
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 65, in check_Fermat
    theorem_test(int_a,int_b,int_c,int_n)
NameError: name 'int_n' is not defined
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 65, in check_Fermat
    theorem_test(int_a,int_b,int_c,exponent_n)
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 4, in theorem_test
    if exponent_n>2 and (int_a**int_n)+(int_b**exponent_n)==(int_c**exponent_n):
NameError: name 'int_n' is not defined
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
Sorry, that combination doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":1
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":.5
Enter a value for "n":2
Well that's not what the theorem was claiming...
>>> 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":2.01
Traceback (most recent call last):
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 52, in check_Fermat
    exponent_n = int(n) #test if the value of n is an integer type
ValueError: invalid literal for int() with base 10: '2.01'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 56, in check_Fermat
    if n>2:
TypeError: '>' not supported between instances of 'str' and 'int'
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
Sorry, that combination doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":1
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":2.01
n= 3
Sorry, that combination doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":1.99
n= 1.99
Well that's not what the theorem was claiming...
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":1.99
n= 1
Well that's not what the theorem was claiming...
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":1.99
Traceback (most recent call last):
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 52, in check_Fermat
    exponent_n = int(n) #test if the value of n is an integer type
ValueError: invalid literal for int() with base 10: '1.99'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 57, in check_Fermat
    if exponent_3>n>2:
NameError: name 'exponent_3' is not defined
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":1.99
n= 1
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":2.01
n= 3
Sorry, that combination doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":2
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":a
You need to input only numbers if you want this to work...
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 66, in check_Fermat
    theorem_test(int_a,int_b,int_c,exponent_n)
UnboundLocalError: local variable 'exponent_n' referenced before assignment
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":a
You need to input only numbers if you want this to work...
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":1
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 66, in check_Fermat
    theorem_test(int_a,int_b,int_c,exponent_n)
UnboundLocalError: local variable 'int_a' referenced before assignment
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":1
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":2
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
Sorry, that combination doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":a
You need to input only numbers if you want this to work...
Enter a value for "c":b
You need to input only numbers if you want this to work...
Enter a value for "n":1
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 66, in check_Fermat
    if isinstance(int_a, int) and isinstance(int_b, int) and isinstance(int_c, int) and (isinstance(exponent_n,int) or isinstance(exponent_n,float)):
UnboundLocalError: local variable 'int_b' referenced before assignment
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":a
You need to input only numbers if you want this to work...
Enter a value for "c":2
Enter a value for "n":3
Sorry, one of your values was not a number. Please try again.
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":4
Enter a value for "b":d
You need to input only numbers if you want this to work...
Enter a value for "c":1
Enter a value for "n":2
Sorry, one of your values was not a number. Please try again.
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":1
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":a
You need to input only numbers if you want this to work...
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    check_Fermat()
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py", line 67, in check_Fermat
    if isinstance(int_a, int) and isinstance(int_b, int) and isinstance(int_c, int) and (isinstance(exponent_n,int) or isinstance(exponent_n,float)):
UnboundLocalError: local variable 'int_a' referenced before assignment
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":a
You need to input only numbers if you want this to work...
Enter a value for "c":2
Enter a value for "n":3
Sorry, one of your values was not a number. Please try again.
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 

 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise5_2_Question2.py 
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":a
You need to input only numbers if you want this to work...
Enter a value for "n":4
Sorry, one of your values was not a number. Please try again.
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":4
Sorry, that combination doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":1
Enter a value for "n":5
Sorry, that combination doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":1
Well that's not what the theorem was claiming...
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":2
Enter a value for "c":3
Enter a value for "n":2.1
n= 3
Sorry, that combination doesn't work.
>>> check_Fermat()
Consider the equation a^n + b^n = c^n. This test will check if Fermat's last theorem is true based on four user inputs: a, b, c, and n.
Enter a value for "a":1
Enter a value for "b":1
Enter a value for "c":1
Enter a value for "n":1.899
n= 1
Well that's not what the theorem was claiming...
>>> 
