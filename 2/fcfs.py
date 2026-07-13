import matplotlib.pyplot as plt

n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    pid = "P" + str(i + 1)
    at = int(input(f"Enter Arrival Time of {pid}: "))
    bt = int(input(f"Enter Burst Time of {pid}: "))
    processes.append([pid, at, bt])

# Sort according to Arrival Time
processes.sort(key=lambda x: x[1])

time = 0
gantt = []

totalWT = 0
totalTAT = 0

for p in processes:

    pid, at, bt = p

    if time < at:
        time = at

    ct = time + bt
    tat = ct - at
    wt = tat - bt

    p.extend([ct, tat, wt])

    gantt.append((pid, time, bt))

    totalWT += wt
    totalTAT += tat

    time = ct

print("\nFCFS Scheduling\n")

print("Process\tAT\tBT\tCT\tTAT\tWT")

for p in processes:
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}\t{p[5]}")

print("\nAverage Waiting Time =", totalWT / n)
print("Average Turnaround Time =", totalTAT / n)

# Gantt Chart
fig, ax = plt.subplots(figsize=(8,2))

for pid, start, bt in gantt:
    ax.broken_barh([(start, bt)], (10,8))
    ax.text(start + bt/2, 14, pid, ha='center')

times = [0]
for _, start, bt in gantt:
    times.append(start + bt)

ax.set_xlim(0, time)
ax.set_ylim(5,25)
ax.set_xlabel("Time")
ax.set_yticks([])
ax.set_xticks(times)
ax.set_title("FCFS Gantt Chart")

plt.grid(axis="x")
plt.show()