
def grade_to_int(s):
    if s.lower() == "a":
        return 5
    if s.lower() == "b":
        return 4.5
    if s.lower() == "c":
        return 4
    if s.lower() == "d":
        return 3.5
    if s.lower() == "e":
        return 3
    return 0

line = raw_input("> ")

data = line.split("+")

totpoints = 0
total = 0
for x in data:
    if x:
        points = float(x[:-1])
        totpoints += points
        total += points * grade_to_int(x[-1])

print total / float(totpoints)
