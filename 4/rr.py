import matplotlib.pyplot as plt

n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    pid = "P" + str(i + 1)
    at = int(input(f"Enter Arrival Time of {pid}: "))
    bt = int(input(f"Enter Burst Time of {pid}: "))
    processes.append([pid, at, bt, bt])   # Remaining Time = BT

tq = int(input("Enter Time Quantum: "))

time = 0
completed = 0

available = []
gantt = []

while completed < n:

    # Add newly arrived processes
    for p in processes:
        if p[1] <= time and p not in available and p[3] > 0:
            available.append(p)

    # If CPU is idle
    if len(available) == 0:
        time += 1
        continue

    # Take first process
    current = available.pop(0)

    pid,at,bt,rt= current

    # Execute process
    if rt > tq:
        gantt.append((pid, time, tq))
        current[3] -= tq
        time += tq
    else:
        gantt.append((pid, time, rt))
        time += rt
        current[3] = 0

        ct = time
        tat = ct - at
        wt = tat - bt

        current.extend([ct, tat, wt])

        completed += 1

    # Add newly arrived processes during execution
    for p in processes:
        if p[1] <= time and p not in available and p[3] > 0 and p != current:
            available.append(p)

    # Put process back if not completed
    if current[3] > 0:
        available.append(current)

print("\nRound Robin Scheduling\n")

print("Process\tAT\tBT\tCT\tTAT\tWT")

totalWT = 0
totalTAT = 0

processes.sort()

for p in processes:
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[4]}\t{p[5]}\t{p[6]}")
    totalWT += p[6]
    totalTAT += p[5]

print("\nAverage Waiting Time =", totalWT / n)
print("Average Turnaround Time =", totalTAT / n)

# Gantt Chart

fig, ax = plt.subplots(figsize=(10, 2))

for pid, start, bt in gantt:
    ax.broken_barh([(start, bt)], (10, 8))
    ax.text(start + bt/2, 14, pid, ha="center")

times = [0]
for _, start, bt in gantt:
    times.append(start + bt)

ax.set_xlim(0, time)
ax.set_ylim(5, 25)
ax.set_xlabel("Time")
ax.set_yticks([])
ax.set_xticks(times)
ax.set_title("Round Robin Gantt Chart")

plt.grid(axis="x")
plt.show()