import sys, math

for line in sys.stdin:
    x = [int(x) for x in line.split(" ")]

print int(math.ceil(x[0] / math.sin (math.radians(x[1]))))
