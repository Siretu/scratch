import sys

for line in sys.stdin:
    pass

line = line.strip()
last = 0
splits = []
for i in range(2):
    for j in range(last,len(line)-1):
        if line[j] < line[last]:
            last = j
    splits.append(last)
    last += 1

parts = []

parts.append(line[:splits[0]+1])
parts.append(line[splits[0]+1:splits[1]+1])
parts.append(line[splits[1]+1:])

parts = [x[::-1] for x in parts]
result = "".join(parts)

print result
