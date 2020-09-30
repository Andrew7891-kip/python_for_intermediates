# threads: is an entity within a process that can be scheduled
# process : is an instance of a program
from threading import Thread
import time


database_value = 0

def increase():
    global database_value
    local_copy = database_value
    local_copy +=1
    time.sleep(0.1)
    database_value=local_copy

if __name__ == "__main__":

    print('start value',database_value)

    t1 = Thread(target=increase)    
    t2 = Thread(target=increase) 

    t1.start()   
    t2.start()

    t1.join()   
    t2.join()

    print('end_value',database_value)

    print('end')   
    