# floating point 0-1
import random
import secrets

k= secrets.randbelow(10)
print(k)


a=random.random()
print(a)

# random float that has a range
b= random.uniform(1,10)
print(b)

# random integer
# has end points
c = random.randint(1,10)
print(c)

# contain range but can't output the right end
d = random.randrange(1,10)
print(d)

# random numbers with a normal distribution 
# exp: 0-mean, 1-std
e= random.normalvariate(0,1)
print(e)

# random sequence
mylist= list('Andrew')
f= random.choice(mylist)
print(f)

# random sequence: more elements
g = random.sample(mylist,3)
print(g)

# random sequence: more elements picked twice
h = random.choices(mylist ,k=3)
print(h)

# shuffle the sequence
j=list('kiprono')
random.shuffle(j)
print(j)

# applications of random
import numpy as np

s= np.random.rand(3,4)

q = np.random.randint(0,10,(3,2))

arr = np.array([[1,2,3],[5,4,3],[9,8,7]])

print(arr)

np.random.shuffle(arr)

print(arr)

print(q)

print(s)