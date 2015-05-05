import re
prog = re.compile(".")
result = prog.findall("foobar")
print result
