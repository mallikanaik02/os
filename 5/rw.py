import threading
import time
import random

# Semaphores
mutex = threading.Semaphore(1)
write = threading.Semaphore(1)

read_count = 0

# Reader Function
def reader(id):
    global read_count

    mutex.acquire()
    read_count += 1

    if read_count == 1:
        write.acquire()      # First reader blocks writers

    mutex.release()

    print(f"Reader {id} is reading...")
    time.sleep(random.randint(1,3))
    print(f"Reader {id} finished reading.")

    mutex.acquire()
    read_count -= 1

    if read_count == 0:
        write.release()      # Last reader allows writers

    mutex.release()


# Writer Function
def writer(id):

    write.acquire()

    print(f"Writer {id} is writing...")
    time.sleep(random.randint(2,4))
    print(f"Writer {id} finished writing.")

    write.release()


# Create Threads
threads = []

# Readers
for i in range(3):
    t = threading.Thread(target=reader, args=(i+1,))
    threads.append(t)

# Writers
for i in range(2):
    t = threading.Thread(target=writer, args=(i+1,))
    threads.append(t)

# Start Threads
for t in threads:
    t.start()

# Wait for Completion
for t in threads:
    t.join()

print("\nExecution Completed")