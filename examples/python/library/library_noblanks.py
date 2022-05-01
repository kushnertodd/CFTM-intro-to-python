lines = []
with open('library_all.txt') as f:
    lines = f.readlines()

blank_count = 0
nonblank_count = 0
count = 0
nonblanks = []
sawblank = 1
for line in lines:
    count += 1
    if len(line) > 1:
        if sawblank == 1:
            nonblanks.append(line)
            sawblank = 0
    else:
        sawblank = 1
print("")
print("nonblanks")
for line in nonblanks:
    print(line, end="")
