frames = int(input("Enter number of frames: "))
ref = list(map(int, input("Enter reference string: ").split()))

memory = []
recent = []
faults = 0

print("\nPage\tFrames")

for page in ref:

    if page in memory:
        recent.remove(page)
        recent.append(page)

    else:
        faults += 1
        if len(memory) < frames:
            memory.append(page)
        else:
            lru = recent.pop(0)
            index = memory.index(lru)
            memory[index] = page

        recent.append(page)
    print(page, "\t", memory)

print("\nTotal Page Faults =", faults)