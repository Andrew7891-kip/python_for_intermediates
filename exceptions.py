# error and exceptions
# syntax error:
# a=2 print(a)

# type error:
# b= 2+'4'

# module not found error:
# import hhh

# name error:
# b=3
# c=d

# file not found error:
# f=open('2.docx')

# value error:
# a= [1,2,3]
# a.remove(5)

# index error:
# a[6]

# key error:
# my={'name':'Andrew'}
# my['age']

# exception

# class 
class Valuetooerror(Exception):
    pass

def test(x):
    if x>100:
        raise Valuetooerror('too high')
try:
    test(200)
except Valuetooerror as e:
    print(e)

# if statement
x=4
if x>0:
    raise Exception('x should be negative')

# assertion
assert (x>0), 'x should be negative'

# try/except
try:
    a= 5/0
except Exception as e:
    print(e)

finally:
    print('cleaning up')