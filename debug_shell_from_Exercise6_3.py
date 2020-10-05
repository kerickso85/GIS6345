Python 3.6.9 |Anaconda, Inc.| (default, Jul 30 2019, 14:00:49) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise6_3.py 
>>> middle(test)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    middle(test)
NameError: name 'test' is not defined
>>> middle(to)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    middle(to)
NameError: name 'to' is not defined
>>> middle(the)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    middle(the)
NameError: name 'the' is not defined
>>> first(test)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    first(test)
NameError: name 'test' is not defined
>>> middle('the')
'h'
>>> middle('to')
''
>>> middle('i')
''
>>> middle('')
''
>>> middle()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    middle()
TypeError: middle() missing 1 required positional argument: 'word'
>>> first('test')
't'
>>> first('')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    first('')
  File "C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise6_3.py", line 2, in first
    return word[0]
IndexError: string index out of range
>>> first('t')
't'
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise6_3.py 
>>> is_palindrome('test')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    is_palindrome('test')
TypeError: is_palindrome() takes 0 positional arguments but 1 was given
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>test
Number of characters in the word are:  4
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise6_3.py 
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>bob
Number of characters in the word are:  3
Your word has an even number of characters, therefore it cannot be a palindrome.
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise6_3.py 
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>bob
Number of characters in the word are:  3
You appear to have entered a palindrome
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>test
Number of characters in the word are:  4
Your word has an even number of characters, therefore it cannot be a palindrome.
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>a
Number of characters in the word are:  1
Yes, your single character is technically a palindrome. But a lame one at that...
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>scobbocs
Number of characters in the word are:  8
Your word has an even number of characters, therefore it cannot be a palindrome.
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise6_3.py 
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>scobbocs
Number of characters in the word are:  8
You appear to have entered a palindrome
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>scobtisttsitbocs
Number of characters in the word are:  16
You appear to have entered a palindrome
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>drake
Number of characters in the word are:  5
You don't have a palindrome.
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>doggyyyggod
Number of characters in the word are:  11
You appear to have entered a palindrome
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>doggy1
Number of characters in the word are:  6
You don't have a palindrome.
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>123321
Number of characters in the word are:  6
You appear to have entered a palindrome
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>1233444
Number of characters in the word are:  7
You don't have a palindrome.
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise6_3.py 
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>testesst
Number of characters in the word are:  8
You appear to have entered a palindrome
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise6_3.py 
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>bob
Number of characters in the word are:  3
You appear to have entered a palindrome
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>bookoob
Number of characters in the word are:  7
index: 3
k
o
You appear to have entered a palindrome
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise6_3.py 
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>bookoob
Number of characters in the word are:  7
index: 3
negative index: -3
k
o
You appear to have entered a palindrome
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise6_3.py 
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>bookoob
Number of characters in the word are:  7
index: 3
negative index: -3
k
o
index: 4
negative index: -4
o
k
You appear to have entered a palindrome
>>> 
 RESTART: C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 3/Exercise6_3.py 
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>bookoob
Number of characters in the word are:  7
index: 3
negative index: -3
o
o
index: 4
negative index: -4
k
k
You appear to have entered a palindrome
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>tesstests
Number of characters in the word are:  9
You don't have a palindrome.
>>> is_palindrome()
Please enter a single word to determine if it is a palindrome:
>>>biglongworddrowgnolgib
Number of characters in the word are:  22
index: 3
negative index: -3
g
g
index: 4
negative index: -4
l
l
index: 5
negative index: -5
o
o
index: 6
negative index: -6
n
n
index: 7
negative index: -7
g
g
index: 8
negative index: -8
w
w
index: 9
negative index: -9
o
o
index: 10
negative index: -10
r
r
index: 11
negative index: -11
d
d
index: 12
negative index: -12
d
d
You appear to have entered a palindrome
>>> 
