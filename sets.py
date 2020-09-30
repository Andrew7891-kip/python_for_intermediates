# sets: mutable,no duplicates,unordered
print('===1===')
myset=set('ronnie')
print(myset)

print('===2===')
myset.pop()
print(myset)

print('===3===')
# union and intersection and difference
odds={1,3,5,7,9}
even={2,4,6,8}
prime={2,3,5,7}


u=odds.union(even)
print(u)

print('====')
i=odds.intersection(prime)
print(i)

print('====')
d=odds.difference(prime)
print(d)

print('====')
s_D=odds.symmetric_difference(prime)
print(s_D)

print('====')
print(even.issubset(odds))

