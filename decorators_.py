# decorator: adds a new function to an existing function
# function decorator
# class decorator
import functools


def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('start')
        results= func(*args,**kwargs)
        print('stop')
        return results
    return wrapper

@start_end_decorator
def add4(x):
    return x+4

results = add4(10)
print(results)


print(add4.__name__)


def repeat(num_times):
    def decorators_repeat(func):

        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                results = func(*args,**kwargs)
            return results
        return wrapper
    return decorators_repeat

# using multiple decorators
@start_end_decorator
@repeat(num_times=4)
def greet(name):
    print(f'hello {name} ')

greet('Andrew')



# ======class decorators=====
class Countcalls:

    def __init__(self,func):
        self.func = func
        self.num_call = 0

    def __call__(self,*args,**kwargs):
        self.num_call += 1
        print(f'this is executed {self.num_call} times ')
        return self.func(*args,**kwargs)

@start_end_decorator
@Countcalls
def say_hello():
    print('hello')

say_hello()
say_hello()
say_hello()
say_hello()
