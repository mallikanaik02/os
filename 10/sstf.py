import matplotlib.pyplot as plt

requests = list(map(int, input("enter req sep by space ").split()))

head = int(input("Enter initial head position: "))

sequence = [head]
total_seek = 0
current = head

while len(requests) > 0:  

    nearest = requests[0]

    for r in requests:
        if abs(current - r) < abs(current - nearest):
            nearest = r

    total_seek += abs(current - nearest)
    current = nearest

    sequence.append(current)
    requests.remove(nearest)

print("\nOrder of Service:")
print(" -> ".join(map(str, sequence)))

print("\nTotal Head Movement =", total_seek)

# -------- Graph --------

plt.figure(figsize=(8,4))

x = list(range(len(sequence)))

plt.plot(x, sequence, marker='o')

plt.xticks(x)
plt.xlabel("Order of Requests")
plt.ylabel("Disk Track Number")
plt.title("SSTF Disk Scheduling")

plt.grid(True)

plt.show()