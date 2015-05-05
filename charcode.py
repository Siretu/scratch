import sys

foo = " ".join(sys.argv[1:])

print foo

print "String.fromCharCode(%s)" % ",".join(str(ord(x)) for x in list(foo))
