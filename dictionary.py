# dictionary: key-value pairs,unordered mutable
# closed by curly_braces
print('--1--')
mydict={'name':'Andrew','age':19,'employed':False}
print(mydict)
# or 
my_dict=dict(name='Andrew',age=19,employed=False)
print(my_dict)

print('--2--')
# access
value=my_dict['name']
print(value)

print('--3--')
# edit
my_dict['email']='max@gmail.com'
print(my_dict)

print('--4--')
# delete
del my_dict['email']
print(my_dict)

# or remove last item
mydict.popitem()
print(mydict)

print('--5--')
# check
try:
    print(my_dict['lname'])
except:
    print(ValueError('no such key'))

print('--6--')
# looping key
for i in my_dict.keys():
    print(i)

print('-----')
# looping value
for i in my_dict.values():
    print(i)

print('-----')
# looping key and value
for i,j in my_dict.items():
    print(i,j)

print('--7--')
# match
my=dict(date=1,month='january',year=2020)
my.update(my_dict)
print(my)