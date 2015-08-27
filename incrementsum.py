# Add two numbers using += 1, but without the + operator
def add(a,b):
    negative = False
    if b < 0:
        negative = True

    for _ in range(abs(b)):
        if negative:
            a -= 1
        else:
            a += 1

    return a


print add(3,5)
print add(-3,5)
print add(3,-5)
print add(-3,-5)
print
print 8
print 2
print -2
print -8
