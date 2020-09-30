# closed by square brackets
# separated by a comma
# accepts all elements: bool,str,int
print('====001====')
mylist=['managu','sukuma','nyanya']
print(mylist)

print('====002====')
# accessed by index
print(mylist[0])

print('====003====')
# iteration
for i in mylist:
    print(i)

print('====004====')
# checking
if 'managu' in mylist:
    print('yes')
else:
    print('no')

print('====005====')
# check size
print(len(mylist))

print('====006====')
# adding item in list
mylist.append('avocado')
mylist.append('cabbage')
print(mylist)

print('====007====')
# adding element at specific index
mylist.insert(2,'ugali')
mylist.insert(4,'royco')
print(mylist)

print('====008====')
# remove last item
item=mylist.pop()
print(item)
print(mylist)

print('====009====')
# remove specific item
mylist.remove('nyanya')
print(mylist)

print('====010====')
# reverse items
items=mylist.reverse()
print(items)

print('====011====')
# sort
o=[9,2,1,5,3,4,6]
print(o.sort())

print('====012====')
# slicing
listi=[6,8,2,4,8,9]
a=listi[:4]
print(a)

print('====013====')
# list comprehension(square all the elements)
d=[9,5,1,4,5]
h=[i*i for i in d]
print(d)
print(h)



