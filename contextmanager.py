# context manager allows you to allocate and release resources when needed


with open ('notes.txt','w') as file:
    file.write('hello world')
# when terminating the file it creates and saves the data in a file 
# without calling the closing function

class File:
    def __init__(self,filename):
        self.filename=filename

    def __enter__(self):
        print('enter')
        self.file=open(self.filename,'w')
        return self.file

    def __exit__(self,e_type,e_value,e_traceback):
        if self.file:
            self.file.close()
        if e_type is not None:
            print('exception has been handled')
        # print('exc: ',e_type,e_value)
        print('exit')
        return True

with File('rep.txt') as file:
    file.write('hello, how are you?')
    file.hdj()
print('continue')

# import module 
# from contextlib import contextmanager

from contextlib import contextmanager

@contextmanager
def file_manager(filename):
    f = open(filename,'w')
    try:
        yield f
    finally:
        f.close()

with file_manager('name.txt') as f:
    f.write('hello')