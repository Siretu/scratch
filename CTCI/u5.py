# 5.1 Insert M into N between bit i and j.
def insert(N,M,i,j):
    return (M << i) | N
    

# 5.2 Print a real number between 0 and 1 in binary representation
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

# 5.3 Print the next smallest and largest number with same amount of 1 bits
# Misinterpreted question and forgot part about keeping same amount of bits.
def print_binary(b):
    print int("".join(b),2)

def onebits(i):
    binary = list(bin(i)[2:])# Convert to binary and remove prefix
    print binary
    first_zero = -1
    for i,bit in enumerate(binary):
        if bit == "0":
            first_zero = i

    if first_zero == -1:
        print_binary(list("1"+ "0" * len(binary)))
        binary[len(binary)-1] = "0"
        print_binary(binary)
        return

    binary[first_zero] = "1" 
    binary2 = binary[:]
    if first_zero > 0:
        binary[first_zero-1] = "0"
    else:
        binary = ["1"] + binary
    if first_zero < len(binary2) - 1:
        binary2[first_zero+1] = "0"

    print_binary(binary2)
    print_binary(binary)


# 5.4 Determine the number of bits required to convert integer a to integer b
def convert(a, b):
    difference = bin(a ^ b)[2:] # Make sure to remove '0b' prefix
    return sum([int(x) for x in difference])

