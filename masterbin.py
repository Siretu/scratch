target = 11

def elgerbeslut(K):
    print "Called with %d" % K
    return target > K

def optelger():
    mini = 1
    maxi = 10
    while mini < maxi:
        print "[%d..%d]" % (mini,maxi)
        M = (mini+maxi)/2
        if elgerbeslut(M):
            mini = M + 1
        else:
            maxi = M
    return mini

print optelger()
