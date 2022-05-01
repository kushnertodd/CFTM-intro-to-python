f = open("dict.txt")
g = open("dict5.txt", "w")
for l in f:
    s = l.strip()
    if len(s) == 5:
        g.write(f'{s}\n')
f.close()
