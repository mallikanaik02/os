import matplotlib.pyplot as plt

n = int(input("Enter number of disk requests: "))

requests = []

print("Enter the disk requests:")
for i in range(n):
    requests.append(int(input()))

head = int(input("Enter initial head position: "))

sequence = [head]
total_seek = 0
current = head

# FCFS Scheduling
for req in requests:
    total_seek += abs(current - req)
    current = req
    sequence.append(req)

print("\nOrder of Service:")
print(" -> ".join(map(str, sequence)))

print("\nTotal Head Movement =", total_seek)

# -------- Head Movement Chart --------

plt.figure(figsize=(8,4))

x = list(range(len(sequence)))

plt.plot(x, sequence, marker='o')

plt.xticks(x)
plt.xlabel("Order of Requests")
plt.ylabel("Disk Track Number")
plt.title("FCFS Disk Scheduling")

plt.grid(True)

plt.show()