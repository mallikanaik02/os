frames = int(input("Enter number of frames: "))
ref = list(map(int, input("Enter reference string: ").split()))

memory = []
faults = 0

print("\nPage\tFrames")

i = 0

for page in ref:

    if page not in memory:
        faults += 1

        if len(memory) < frames:
            memory.append(page)

        else:

            farthest = -1
            replace = 0

            for j in range(frames):

                # Page will never be used again
                if memory[j] not in ref[i+1:]:
                    replace = j
                    break

                future = ref[i+1:].index(memory[j])

                if future > farthest:
                    farthest = future
                    replace = j

            memory[replace] = page

    print(page, "\t", memory)

    i += 1

print("\nTotal Page Faults =", faults)