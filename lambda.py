# lambda arguements: expression
# shorter function than def
# exp1
# normal func:
def add4(d):
    return d+4
print(add4(5))

# lambda func:
add3= lambda x: x+3
print(add3(7))

# can take multiple func
mult = lambda x,y: x/y
print(mult(4,2))

# lambda: sorted
points = [(1,2),(3,5),(8,9),(0,3),(91,2)]
# sorted
p_sort= sorted(points)

# lambda sort
p1_sort= sorted(points,key= lambda x: x[0] + x[1])
print(p_sort)
print(p1_sort)

# map(func,seq)
a= [3,2,1,4]
b= map(lambda x: x**2,a)
print(list(b))
# or
# brings same func
c =[x**2 for x in a]
print(c)

# filter func
# odd numbers
d= filter(lambda x: x%2 != 0,a)
print(list(d))

# or
# results: bool
e= [x%2 != 0 for x in a]
print(e)
# results : odd
f= [x for x in a if x%2 != 0]
print(f)

# reduce func
from functools import reduce
g= reduce (lambda x,y: x*y,a)
print(g)
