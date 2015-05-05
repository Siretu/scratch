import sys

def reverse_binary(i):
    bin_i = bin(i)[2:] ## Remove the "0b" part at the start
    rev_bin = bin_i[::-1] ## Reverse the binary representation
    rev_i = int(rev_bin,2) ## Convert it back to decimal
    return rev_i

# Minimized one-line version
rev_bin_min = lambda i : int(bin(i)[2:][::-1],2)


for line in sys.stdin:
    x = int(line)
print reverse_binary(x)
print rev_bin_min(x)
