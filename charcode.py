# Just a quick python script to convert a string to ascii values to easily 
# insert into javascript applications for injections.

import sys

foo = " ".join(sys.argv[1:])

print foo

print "String.fromCharCode(%s)" % ",".join(str(ord(x)) for x in list(foo))
