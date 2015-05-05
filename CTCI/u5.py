def insert(N,M,i,j):
    return (M << i) | N
    

def decbin(r):
    result = "0."
    start = 0.5
    while r != 0:
        if len(result) > 32:
            return "ERROR"
        if r >= start:
            result += "1"
            r -= start
        else:
            result += "0"
        start /= 2
    if result == "0.":
        return "0"
    return result

