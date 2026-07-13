import matplotlib.pyplot as plt

n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    pid = "P" + str(i + 1)
    at = int(input(f"Enter Arrival Time of {pid}: "))
    bt = int(input(f"Enter Burst Time of {pid}: "))
    processes.append([pid, at, bt])

completed = []
time = 0
gantt = []

while len(completed) < n:

    available = []

    # Find all arrived processes
    for p in processes:
        if p[1] <= time and p[0] not in completed:
            available.append(p)

    # If no process has arrived
    if len(available) == 0:
        time += 1
        continue

    # Find process with smallest Burst Time
    shortest = available[0]

    for p in available:
        if p[2] < shortest[2]:
            shortest = p

    pid = shortest[0]
    at = shortest[1]
    bt = shortest[2]

    start = time
    ct = start + bt
    tat = ct - at
    wt = tat - bt

    shortest.extend([ct, tat, wt])

    gantt.append((pid, start, bt))
    completed.append(pid)

    time = ct

# Display Table
print("\nSJF (Non-Preemptive)\n")
print("Process\tAT\tBT\tCT\tTAT\tWT")

totalWT = 0
totalTAT = 0

# Sort by Process ID
processes.sort()

for p in processes:
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}\t{p[5]}")
    totalWT += p[5]
    totalTAT += p[4]

print("\nAverage Waiting Time =", totalWT / n)
print("Average Turnaround Time =", totalTAT / n)

# -------- Gantt Chart --------

fig, ax = plt.subplots(figsize=(8,2))

for pid, start, bt in gantt:
    ax.broken_barh([(start, bt)], (10, 8))
    ax.text(start + bt/2, 14, pid, ha='center')

times = [0]
for _, start, bt in gantt:
    times.append(start + bt)

ax.set_xlim(0, time)
ax.set_ylim(5, 25)
ax.set_xlabel("Time")
ax.set_yticks([])
ax.set_xticks(times)
ax.set_title("SJF Gantt Chart")

plt.grid(axis="x")
plt.show()