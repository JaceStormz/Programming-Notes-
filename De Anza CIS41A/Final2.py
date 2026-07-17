amList = []
pmList = []

for line in f:
    parts = line.strip().split(": ")
    time = parts[-1]

    if time.endswith("am"):
        amList.append(time[:-2])
    elif time.endswith("pm"):
        pmList.append(time[:-2])

pmList = ["3:30", "3:30", "6:00", "1:30", "3:30", "1:30", "1:30"]

counts = {}

for time in pmList:
    counts[time] = counts.get(time, 0) + 1

for time in sorted(counts):
    print(time, counts[time])