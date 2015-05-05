import sys

inp = []
for line in sys.stdin:
    inp.append(line)

a = [int(x) for x in inp[1].split()]

b = a[:]
b.sort()

def permutation(a,b):
    target = []
    for x in range(len(a)):
        for y in range(len(b)):
            if a[x] == b[y] and y not in target:
                target.append(y)
                break

    return target

def number_of_swaps(permutation):
    swaps = []
    seen = set()
    for i in xrange(len(permutation)):
        if i not in seen:           
           j = i
           while permutation[j] != i:
               swaps.append([j,permutation[j]])
               j = permutation[j]
               seen.add(j)
    return swaps


foo = permutation(a,b)
bar = number_of_swaps(foo)
print len(bar)
if len(bar):
    print "\n".join([" ".join([str(y) for y in x]) for x in bar])

