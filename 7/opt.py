frames = int(input("Enter number of frames: "))
ref = list(map(int, input("Enter reference string: ").split()))

memory = []
faults = 0

print("\nPage\tFrames")

for i in range(len(ref)):

    page = ref[i]

    if page not in memory:

        faults += 1

        if len(memory) < frames:
            memory.append(page)

        else:

            farthest = -1
            index = -1

            for j in range(len(memory)):

                if memory[j] not in ref[i+1:]:
                    index = j
                    break

                future = ref[i+1:].index(memory[j])

                if future > farthest:
                    farthest = future
                    index = j

            memory[index] = page

    print(page, "\t", memory)

print("\nTotal Page Faults =", faults)