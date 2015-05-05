def alphsort(l):
    d = {}
    for i in range(97,123):
        d[chr(i)] = 0

    for c in l:
        if c not in d:
            raise Exception
        else:
            d[c] = d[c] + 1

    result = []
    for i in range(97,123):
        result += [chr(i)]*d[chr(i)]

    return result
