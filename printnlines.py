# Print x last lines in string/file


str1 = "str1\nstr2\nstr3\nstr4\nstr5\nstr6\nstr7\nstr8\nstr9\nstr10\nstr11\nstr12\nstr13\nstr14\nstr15\nstr16\nstr17\nstr18\nstr19\nstr20\nstr21\nstr22\nstr23\nstr24\nstr25"

def print_last_lines(string, n):
    print "\n".join(string.split("\n")[-n:])

print_last_lines(str1,10)

print_last_lines("",10)
