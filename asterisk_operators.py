# * * * * * * *
# multiplication
print(8*7)

# square ^ values
print(2**4)

# multiple elements
print([8]*10)
print([8,2]*10)
print('an'*10)

# functions arguments(args ,kwargs)
def foo(a,b,*args,**kwargs):
    print(a,b)

    for arg in args:
        print(arg)

    for key in kwargs:
        print(key,kwargs[key])

foo(1,2,3,4,5,six=6,seven=7)

# argument unpacking
def func(a,b,c):
    print(a,b,c)

my_dict={'a':2,'b':5,'c':6}
func(**my_dict)

mylist=[1,2,3]
func(*mylist)

# container unpacking
num=[1,2,3,4,5,6]
*beg,last=num
print(beg)
print(last)

# match iterables to list
my_tuple=(1,2,3)
my_list=[4,5,6]
new_list=(*my_tuple,*my_list)
print(new_list)

# or dictionary matching
dict_a={'a':1,'b':2}
dict_b={'c':3,'d':4}
dict_c={**dict_a,**dict_b}
print(dict_c)
