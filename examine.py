import sys

# gets the average, min and max of summary log files
closed = []
opened = []
with open(sys.argv[1], "r") as file:
    for line in file:
        log, _, num, _ = line.split()
        if "closed" in log:
            closed.append(float(num))
        elif "open" in log:
            opened.append(float(num))
        else:
            raise Exception("Not open nor closed, log file")

for (kind, nums) in [("Closed test", closed), ("Open test", opened)]:
    print(kind)
    print("Min: {}".format(min(nums)))
    print("Max: {}".format(max(nums)))
    print("Mean: {}".format(sum(nums)/len(nums)))