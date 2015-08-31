import sys

l = [(3,4),(8,15),(1,3),(2,5)]

"""
Given a set of intervals, return the larget continuous interval made
from the sub intervals.
"""

def get_maximum_interval(l):
    l.sort()

    # Pick first element and remove from list
    start = l[0][0]
    end = l[0][1]
    l = l[1:]
    max_interval = (start, end)

    for i,x in enumerate(l):
        if x[0] <= end and x[1] > end:
            # We found an overlapping interval with a larger end-point
            end = x[1]
        if x[0] > end and max_interval[1] - max_interval[0] < end - start:
            # End of overlapping intervals. Updating max and starting new.
            max_interval = (start, end)
            start = x[0]
            end = x[1]

    if max_interval[1] - max_interval[0] < end - start:
        max_interval = (start, end)
    return max_interval


print get_maximum_interval(l)
