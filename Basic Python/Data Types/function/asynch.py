# Python Async Example

import asyncio

async def task1():
    print("Task 1 start")
    await asyncio.sleep(3)
    print("Task 1 end")

async def task2():
    print("Task 2 start")
    print("Task 2 end")
    
async def main():
    await asyncio.gather(task1(), task2())
    
asyncio.run(main())