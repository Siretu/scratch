# Small script for thesis work to parse stocks.

def load_history():
    data = ""
    with open("history") as myfile:
        data = myfile.read()
    lines = data.split("\n")
    result = [x.split(",")[1] for x in lines]
    return result

def zipdata(l1,l2):
    current = l1[0]
    """for x in range(1,len(l2)):
        if l2[x] == current:
            l2[x] = 0
        else:
            current = l2[x]"""
    data = load_history()
    l3 = [int(data[x]) for x in l1]
    first = zip(l3,l2)
    result = [[x[0],x[1]] for x in first]
    return result
