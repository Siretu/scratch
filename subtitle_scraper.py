# Intended as a way to scrape subtitle files for occurences of words to be able
# to extract individual words from movies.

from datetime import datetime
import time

occurences = {}

def timedelta_milliseconds(td):
    return td.days*86400000 + td.seconds*1000 + td.microseconds/1000

def parse_time(s):
    t = datetime.strptime(s,"%H:%M:%S,%f")
    t -= t.replace(hour=0, minute=0, second=0, microsecond=0)
    return timedelta_milliseconds(t)

def parse_interval(s):
    times = s.split(" --> ")
    return [parse_time(x) for x in times]


def dict_add(d, key, val):
    if key in d.keys():
        d[key].append(val)
    else:
        d[key] = [val]

def handle_subtitle(s):
    lines = s.split("\n")
    time = parse_interval(lines[0].strip())

    # Join the rows, make all punctuation into space and then split into words and make all the words lowercase
    # I was too lazy to use regex.
    words = [x.lower() for x in " ".join(lines[1:]).replace(","," ").replace("."," ").replace("?"," ").replace("!"," ").split(" ")]
    print "Got subtitle:\n----------\n " + s + "\n------------"
    step = (time[1] - time[0]) / len(words)
    print "Stepping %f" % step
    start = time[0]
    for w in words:
        if w:
            dict_add(occurences,w,start)
            start += step
        


f = open("subtitles.txt")
text = f.read().split("\n")


current = ""
for line in text:
    if "-->" in line:
        current = line
    elif line == "":
        if current != "":
            handle_subtitle(current)
        current = ""
    else:
        current += "\n" + line


print occurences
