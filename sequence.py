
# Groups list by neighboring equal numbers. [1,1,1,2,2,3,1,1] => [[1,1,1],[2,2],[3],[1,1]]
def group(l):
    groups = []
    if l:
        current = [l[0]]
        for x in l[1:]:
            if x != current[0]:
                groups.append(current)
                current = [x]
            else:
                current.append(x)
        groups.append(current)
    return groups

# Compresses a number. 1211 can be seen as "one 1, one 2, two 1's", e.g 111221
def compress(num):
    g = group(str(num))
    result = "".join([str(len(x)) + x[0] for x in g])
    return int(result)

# Returns the nth number in the sequence 1,11,21,1211,111221,312211 
# where each number is the compression of the previous one.
def seq(n):
    current = 1
    while n > 1:
        current = compress(current)
        n -= 1
    return current
    
    
    
