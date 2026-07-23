import matplotlib.pyplot as plt

requests = list(map(int, input("enter req sep by space ").split()))

head = int(input("Enter initial head position: "))

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

if direction == "right":

    # Move Right
    for r in right:
        total_seek += abs(current - r)
        current = r
        sequence.append(current)

    # Reverse and Move Left
    for r in reversed(left):
        total_seek += abs(current - r)
        current = r
        sequence.append(current)

else:

    # Move Left
    for r in reversed(left):
        total_seek += abs(current - r)
        current = r
        sequence.append(current)

    # Reverse and Move Right
    for r in right:
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
plt.title("LOOK Disk Scheduling")

plt.grid(True)
plt.show()