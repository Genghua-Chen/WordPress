import sys
import re


for line in sys.stdin:

    line = line.strip()
    line = re.sub('\W+', ' ', line)
    line = line.lower()
    words = line.split()

    for word in words:

        print ('%s\t%s' % (word, 1))
