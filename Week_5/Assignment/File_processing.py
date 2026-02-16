'''
Question 2: Async File Processing System 

Create an async program that simulates processing multiple large files concurrently:
Write 3 async functions:
read_file_async(filename) - Simulates reading a file (use asyncio.sleep() for 2-5 seconds)
process_file_async(content) - Simulates processing (use asyncio.sleep() for 1-3 seconds)
write_file_async(filename, content) - Simulates writing (use asyncio.sleep() for 1-2 seconds)
Create a main async function that processes 5 files concurrently
Compare execution time with a synchronous version
Print start/end times for each operation to show concurrency
Calculate and display total time saved using async approach
 '''
import asyncio
import time

total_time = 0


class FileException(Exception):
    def __init__(self):
        self.message = "This is a sample exception"
        super().__init__(self.message)


async def file_process(file_name):
    await read_file_async(file_name)
    print("\n")
    await process_file_async(file_name)
    print("\n")
    await write_file_async(file_name, "content")
    print("\n")


async def read_file_async(file_name):
    try:
        print("Started at:", time.perf_counter())
        with open(file_name, "r") as file:
            for line in file:
                print(line)
            await asyncio.sleep(2)
        print("File read successfully")
        print("Finished at:", time.perf_counter())
    except FileException as e:
        print(e, "Error reading file")


async def process_file_async(file_name):
    try:
        print("Started at:", time.perf_counter())
        with open(file_name, "r") as file:
            for line in file:
                print("Processed:", line)
            await asyncio.sleep(1)
        print("File processed successfully")
        print("Finished at:", time.perf_counter())
    except FileException as e:
        print(e, "Error processing file")


async def write_file_async(file_name, content_to_add):
    try:
        print("Started at:", time.perf_counter())
        with open(file_name, "a") as file:
            file.write(content_to_add)
            await asyncio.sleep(2)
        print("File writtern successfully")
        print("Finished at:", time.perf_counter())
    except FileException as e:
        print(e, "Error writing file")


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(file_process("./Text_files/file1.txt"))
        tg.create_task(file_process("./Text_files/file2.txt"))
        tg.create_task(file_process("./Text_files/file3.txt"))
        tg.create_task(file_process("./Text_files/file4.txt"))
        tg.create_task(file_process("./Text_files/file5.txt"))


actual_time = 25
start_time = time.perf_counter()
asyncio.run(main())
total_time = time.perf_counter() - start_time
print("Total Time Saved:", actual_time - total_time)
