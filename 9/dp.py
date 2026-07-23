import threading
import time
import random

n = int(input("Enter number of philosophers: "))

# Create one fork (lock) for each philosopher
forks = []
for i in range(n):
    t=threading.Lock()
    forks.append(t)

def philosopher(i):

    left = forks[i]
    right = forks[(i + 1) % n]

    # Thinking
    print(f"Philosopher {i+1} is Thinking")
    time.sleep(random.randint(1, 2))

    # Hungry
    print(f"Philosopher {i+1} is Hungry")

    # Pick up left fork
    print(f"Philosopher {i+1} is picking up Left Fork")
    left.acquire()

    # Pick up right fork
    print(f"Philosopher {i+1} is picking up Right Fork")
    right.acquire()

    # Eating
    print(f"Philosopher {i+1} is Eating")
    time.sleep(random.randint(1, 2))

    # Put down forks
    print(f"Philosopher {i+1} is putting down Right Fork")
    right.release()

    print(f"Philosopher {i+1} is putting down Left Fork")
    left.release()

    print(f"Philosopher {i+1} finished Eating")
    print(f"Philosopher {i+1} is Thinking again\n")


threads = []

for i in range(n):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All philosophers have finished.")