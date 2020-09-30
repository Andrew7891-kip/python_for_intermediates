# itertools:product,permutation,accumulate,combinations,accumulate,groupby and infinite itertools
from itertools import product,permutations,combinations_with_replacement,combinations,accumulate,groupby
import operator
# product
a=[1,2]
b=[3]

prod=product(a,b, repeat=2)
print(list(prod))

# permutations

c=[1,2,3,4]
perm=permutations(c,4)
print('==================')
print(list(perm))

# combinations

print('=========')
comb=combinations(c,2)
print(list(comb))

print('--------')
combi=combinations_with_replacement(c,2)
print(list(combi))

print('*********')
# adding
acc=accumulate(c)
print(c)
print(list(acc))

print('[[[[[[')
# multiply
accu=accumulate(c,func=operator.mul)
print(c)
print(list(accu))


print('////////')
def smallerthan3(x):
    return x<3

a=[1,2,3,4,5,6]
obj=groupby(a,key=smallerthan3)

# NOTE: we can use lambda function without defining 
# obj=groupby(a,key=lambda x: x<3)
for i,j in obj:
    print(i,list(j))

'................'
student=[{'name':'Andrew','age':20},{'name':'Ryan','age':21}]

gr=groupby(student,key=lambda x: x['age'])

for i,j in gr:
    print(i,list(j))

from itertools import count,cycle,repeat

# count
for i in count(1):
    if i == 10:
        break
    print(i)

# cycle
# f=[1,2,3,4,5]
# for i in cycle(a):
#     print(i)

# repeat
for j in repeat(2,4):
    print(j)

