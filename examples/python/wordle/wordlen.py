import sys
if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} dict-file')
    exit(0)
dict = sys.argv[1]
f = open(dict)
min = 9999
max = 0
for l in f:
    n = len(l.strip())
    if n > max:
        max = n
    if n < min:
        min = n
print(f'{dict}: min {min} max {max}')
