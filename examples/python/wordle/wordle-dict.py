import sys
import re
def inter(s, t):
    for c in s:
        if not c in t:
            return False
    return True

if len(sys.argv) < 4:
    print(f'usage: {sys.argv[0]} dict-file letters fixed')
    exit(0)
dict = sys.argv[1]
letters = sys.argv[2]
fixed = sys.argv[3]
f = open(dict)
for l in f:
    if inter(l.strip(), letters):
        if re.search(fixed, l.strip()):
            #print(f'{l.strip()} {dict}')
            print(f'{l.strip()}')