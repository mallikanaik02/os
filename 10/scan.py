import matplotlib.pyplot as plt

requests = list(map(int, input("enter req sep by space ").split()))

head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))

direction = input("Enter direction (left/right): ").lower()

left = []
right = []

# Divide requests
for r in requests:
    if r < head:
        left.append(r)
    else:
        right.append(r)

left.sort()
right.sort()

sequence = [head]
total_seek = 0
current = head

if direction == "left":

    # Move Left
    for r in reversed(left):
        total_seek += abs(current - r)
        current = r
        sequence.append(current)

    # Go to first track
    total_seek += abs(current - 0)
    current = 0
    sequence.append(current)

    # Move Right
    for r in right:
        total_seek += abs(current - r)
        current = r
        sequence.append(current)

else:

    # Move Right
    for r in right:
        total_seek += abs(current - r)
        current = r
        sequence.append(current)

    # Go to last track
    total_seek += abs(current - (disk_size - 1))
    current = disk_size - 1
    sequence.append(current)

    # Move Left
    for r in reversed(left):
        total_seek += abs(current - r)
        current = r
        sequence.append(current)

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
plt.title("SCAN Disk Scheduling")

plt.grid(True)

plt.show()