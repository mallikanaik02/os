# Banker's Algorithm

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))

allocation = []
maximum = []
need = []

print("\nEnter Allocation Matrix:")
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    allocation.append(row)

print("\nEnter Maximum Matrix:")
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    maximum.append(row)

available = list(map(int, input("\nEnter Available Resources: ").split()))

# Calculate Need Matrix
for i in range(n):
    row = []
    for j in range(m):
        row.append(maximum[i][j] - allocation[i][j])
    need.append(row)

print("\nNeed Matrix:")
for i in range(n):
    print(f"P{i}: {need[i]}")

finish = [False] * n
safe_sequence = []
work = available.copy()

count = 0

while count < n:

    found = False

    for i in range(n):

        if finish[i] == False:

            possible = True

            for j in range(m):
                if need[i][j] > work[j]:
                    possible = False
                    break

            if possible:

                for j in range(m):
                    work[j] += allocation[i][j]

                safe_sequence.append(f"P{i}")
                finish[i] = True
                found = True
                count += 1

    if found == False:
        break

# Result
if count == n:
    print("\nSystem is in SAFE state.")
    print("Safe Sequence:")
    print(" -> ".join(safe_sequence))
else:
    print("\nSystem is NOT in a SAFE state.")
    print("Deadlock may occur.")