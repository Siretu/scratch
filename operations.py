# Takes X numbers and returns a combination of operations and numbers to get the last number as result.
# Does not follow order of operation, but instead just goes left to right. "3 2 1" gives "3 - 2".

import itertools

def operate(symbols, operations):
    stack = symbols[0]
    sym = symbols[::-1][:-1]
    ops = operations[::-1]
    while len(sym) >= 1:
        operator = ops.pop()
        num = float(sym.pop())
        calc = str(stack) + operator + str(num)
        stack = eval(calc)
    return stack

def get_ops(length):
    op = ["+","-","*","/"]
    op_list = [op]*length
    for x in itertools.product(*op_list):
        yield list(x)

def find_answer(syms):
    result = syms[-1]
    inp = syms[:-1]
    op = []
    for x in get_ops(len(inp) - 1):
        res = operate(inp,x)
        if int(res) == result:
            op = x
            break
    if not op:
        print "Invalid"
    else:
        s = ""
        for (i,x) in enumerate(inp):
            s += str(x)
            if i < len(op):
                s+= " %s " % op[i]
        print s

if __name__ == "__main__":
    symbols = raw_input().split(" ")
    symbols = [int(x) for x in symbols]
    find_answer(symbols)
