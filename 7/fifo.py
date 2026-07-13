frames = int(input("Enter number of frames: "))
ref = list(map(int, input("Enter reference string: ").split()))

memory = []
faults = 0
pointer = 0

print("\nPage\tFrames")

for page in ref:

    if page not in memory:
        faults += 1

        if len(memory) < frames:
            memory.append(page)
        else:
            memory[pointer] = page
            pointer = (pointer + 1) % frames

    print(page, "\t", memory)

print("\nTotal Page Faults =", faults)