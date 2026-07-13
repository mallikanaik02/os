import matplotlib.pyplot as plt

n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    pid = "P" + str(i + 1)
    at = int(input(f"Enter Arrival Time of {pid}: "))
    bt = int(input(f"Enter Burst Time of {pid}: "))
    processes.append([pid, at, bt, bt])   # Remaining Time = BT

tq = int(input("\nEnter Time Quantum: "))

time = 0
completed = 0

queue = []
visited = [False] * n
gantt = []

while completed < n:

    # Add newly arrived processes
    for i in range(n):
        if processes[i][1] <= time and not visited[i]:
            queue.append(i)
            visited[i] = True

    if len(queue) == 0:
        time += 1
        continue

    i = queue.pop(0)

    pid = processes[i][0]
    at = processes[i][1]
    bt = processes[i][2]
    rt = processes[i][3]

    # Execute process
    if rt > tq:
        gantt.append((pid, time, tq))
        time += tq
        processes[i][3] -= tq
    else:
        gantt.append((pid, time, rt))
        time += rt
        processes[i][3] = 0

        ct = time
        tat = ct - at
        wt = tat - bt

        processes[i].extend([ct, tat, wt])
        completed += 1

    # Add processes that arrived during execution
    for j in range(n):
        if processes[j][1] <= time and not visited[j]:
            queue.append(j)
            visited[j] = True

    # Add current process back if not completed
    if processes[i][3] > 0:
        queue.append(i)

# Display Table
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

# ---------- Gantt Chart ----------

fig, ax = plt.subplots(figsize=(10,2))

for pid, start, bt in gantt:
    ax.broken_barh([(start, bt)], (10,8))
    ax.text(start + bt/2, 14, pid, ha="center", va="center")

times = [0]
for _, start, bt in gantt:
    times.append(start + bt)

ax.set_xlim(0, time)
ax.set_ylim(5,25)
ax.set_xlabel("Time")
ax.set_yticks([])
ax.set_xticks(times)
ax.set_title("Round Robin Gantt Chart")

plt.grid(axis="x")
plt.show()