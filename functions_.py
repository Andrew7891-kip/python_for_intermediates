# positional arguments
def foo(a,b,c):
    print(a,b,c)

foo(1,2,3)

# keyword arguments
def boo(a,b,c):
    print(a,b,c)

boo(c=3,b=2,a=1)

# positional args with keyword args in same func:
# positional args follows the keyword args
# following function will raise an error: 

# def coo(a,b,c):
#     print(a,b,c)

# boo(c=3,b=2,1)

# def coo(a,b,c):
#     print(a,b,c)

# boo(3,b=2,a=1)

# default args:
# must be at the end of the args
def doo(a,b,c,d=4):
    print(a,b,c,d)

doo(c=3,b=2,a=1)

# variable length args
def bab(a,b,*args,**kwargs):
    print(a,b)

# args
    for i in args:
        print(i)

# kwargs: in dictionary
    for key in kwargs:
        print(key,kwargs[key])

bab(1,2,3,4,5,6,s=7,e=8)

# unpacking args
# works on list[] or tuple() or dictionary
# lenght of key must match with parameter
def cac(a,b,c):
    print(a,b,c)

mylist=(1,2,3)
cac(*mylist)

def dac(a,b,c):
    print(a,b,c)

mylist={'a':1,'b':3,'c':4}
dac(**mylist)

# local vs global variable
def ns():
    x=num
    print(x)

num=0
ns()

# parameter passing
# immutable: not changed 
# mutable: changed
# immutable within mutable can be changed
def par(my_list):
    my_list.append(4)
    my_list[2]=0

a_list=[1,2,3]
par(a_list)
print(a_list)