# tupple allow duplicate element
# it is immutable
# contains two or more items or if one item close it with a comma
# closed by brackets
import sys
import timeit

print('---1---')
mytuple='andrew','brian','audrey','hilda'
print(tuple(mytuple))

print('---2---')
# iteration
for i in mytuple:
    print(i)

print('---3---')
# boolean function
if 'betty' in mytuple:
    print (True)
else:
    print(False)

print('---4---')
# count
print(mytuple.count('andrew'))

print('---5---')
# convert tuple to list and vise verse
i=list(mytuple)
print('--list--')
print(i)

# list to tuple
u=tuple(i)
print('--tuple--')
print(u)


print('---6---')
# unpacking elements
student=('obonyo',20,'kitale')
name,age,city= student

print(name )
print(age )
print(city )

print('---7---')
# compare size of list and tuple in size
# importing sys
mylist=['hello','hi','bonjour']
mytup=('hello','hi','bonjour')

print(sys.getsizeof(mylist),'bytes')
print(sys.getsizeof(mytup),'bytes')
# list is bigger than tuple

print('---8---')
# compare size of list and tuple in time
print(timeit.timeit(stmt='[0,2,6,7]',number=100000))
print(timeit.timeit(stmt='(0,2,6,7)',number=100000))
# list takes longer time than tuple

