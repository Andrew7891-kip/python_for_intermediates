# iterable functions
# save alot of memory
# use of yields
def mygen():
    yield 2
    yield 1
    yield 3

g = mygen()

# sum
print(sum(g))

print(sorted(g))

# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value)

def countdown(num):
    print('starting....')

    while num > 0:
        yield num
        num -=1

cd = countdown(4)
value = next(cd)
print(value)
print(next(cd))
print(next(cd))
print(next(cd))

import sys
# memory efficient:
def firstn(n):
    nums = []
    num=0

    while num < n:
        nums.append(num)
        num += 1
    return nums
print(f'size of functions: {sys.getsizeof(firstn(1000))} ')



# generators
# saves memory
def gen(n):
    num = 0
    while num < n:
        yield num
        num += 1
print(f'size of generators: {sys.getsizeof(gen(1000))}')

def fibonacci(limit):
    a,b = 0,1

    while a < limit:
        yield a
        a,b = b, a+b

fib = fibonacci(10)
for i in (fib):
    print(i)

# expression generators
gene = (i for i in range(10) if i %2==0 )
for i in gene:
    print(i)

# generators
genes = [i for i in range(10) if i %2==0 ]
print(genes)

# IN CONCLUSION GENERATORS SAVES ALOT OF MEMORY,TAKES LESS TIME