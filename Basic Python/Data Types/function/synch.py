#  1. Synchronous Function (Sync) kya hota hai?

import time

def task1():
    print("Task 1 start")
    time.sleep(3)
    print("Task 1 end")
    
def task2():
    print("task 2 start")
    print("task 2 end")

task1()
task2()