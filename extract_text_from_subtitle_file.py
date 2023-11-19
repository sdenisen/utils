import re

with open(file="subtitles.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if re.match("^\d+$", line) or re.match("^\d+.*-->.*\d+$", line):
            continue
        print(line)



