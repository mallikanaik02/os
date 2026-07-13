import matplotlib.pyplot as plt

n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    pid = "P" + str(i + 1)
    at = int(input(f"Enter Arrival Time of {pid}: "))
    bt = int(input(f"Enter Burst Time of {pid}: "))
    processes.append([pid, at, bt, bt])  # Last value is Remaining Time

time = 0
completed = 0
gantt = []
current = None
start = 0

while completed < n:

    available = []

    # Find arrived processes with remaining time
    for p in processes:
        if p[1] <= time and p[3] > 0:
            available.append(p)

    if len(available) == 0:
        time += 1
        continue

    # Find process with shortest remaining time
    shortest = available[0]

    for p in available:
        if p[3] < shortest[3]:
            shortest = p

    # If CPU switches process, save previous Gantt block
    if current != shortest[0]:
        if current is not None:
            gantt.append((current, start, time - start))
        current = shortest[0]
        start = time

    # Execute for 1 ms
    shortest[3] -= 1
    time += 1

    # Process completed
    if shortest[3] == 0:
        ct = time
        tat = ct - shortest[1]
        wt = tat - shortest[2]

        shortest.extend([ct, tat, wt])

        completed += 1

# Add last Gantt block
gantt.append((current, start, time - start))

# Display Table
print("\nSRTF Scheduling\n")

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

# ---------- Gantt Chart ----------

fig, ax = plt.subplots(figsize=(10,2))

for pid, st, bt in gantt:
    ax.broken_barh([(st, bt)], (10,8))
    ax.text(st + bt/2, 14, pid, ha="center", va="center")

times = [0]
for _, st, bt in gantt:
    times.append(st + bt)

ax.set_xlim(0, time)
ax.set_ylim(5,25)
ax.set_xlabel("Time")
ax.set_yticks([])
ax.set_xticks(times)
ax.set_title("SRTF Gantt Chart")

plt.grid(axis="x")
plt.show()