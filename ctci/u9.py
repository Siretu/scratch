def childstair(n):
    ways = {0:0}
    for i in range(1,n+1):
        previous_step = set([max(0,i-1), max(0,i-2), max(0,i-3)])
        ways[i] = sum([ways[x] for x in previous_step])+1
    return ways[n]
