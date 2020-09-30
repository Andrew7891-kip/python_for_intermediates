# process : is an instance of a program
from multiprocessing import Process
import os
import time


def square_num():
    for i in range(10):
        i*i
        time.sleep(0.1)

processes = []

num_process = os.cpu_count()

for i in range(num_process):
    p=Process(target=square_num)
    processes.append(p)

# start
for p in processes:
    p.start()

for p in processes:
    p.join()

print('end main')

