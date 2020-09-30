# collection:counter,namedtuple,ordered_dict,default_dict,deque
from collections import Counter,namedtuple,OrderedDict,deque,defaultdict
a='aaaaddfff'
print('==counter==')
# collection:counter
my_counter=Counter(a)

# counts the characters
print(my_counter)

# prints the most common element in counter
print(my_counter.most_common(1))

print('==named_tuples==')
# collection:namedtuple
# class of point with elements x,y
point=namedtuple('point','x,y')
pt=point(4,5)

print(pt)

print('==orderer_dict==')
# collection:ordereddict
# remembers the order
ordered_dict=OrderedDict()
ordered_dict['b']=2
ordered_dict['d']=4
ordered_dict['c']=3
ordered_dict['a']=1
ordered_dict['e']=5
print(ordered_dict)

print('==defaultdict==')
# collection:defaultdict
d=defaultdict(float)
d['a']=1
d['b']=2

print(d)

print(d['c'])

print('==deque==')
# collection: deque
b=deque()
b.append(1)
b.append(2)
b.append(3)
print(b)

b.pop()

print(b)
b.rotate(-1)
print(b)



