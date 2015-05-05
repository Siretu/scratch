# A "secure" deletion algorithm is defined that inverts the bits in one string n
# times. Check if one string is the first string, inverted n times.

import sys

def inverse(i):
    return "".join([str(1-int(x)) for x in i])

inp = []
for line in sys.stdin:
    inp.append(line.replace("\n",""))

inp[0] = int(inp[0])

if (inp[1] == inp[2] and inp[0] % 2 == 0) or (inp[1] == inverse(inp[2]) and inp[0] % 2 == 1):
    print "Deletion succeeded"
else:
    print "Deletion failed"
