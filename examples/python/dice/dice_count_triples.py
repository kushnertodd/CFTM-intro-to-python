import random

counts = [0, 0]
for die_1 in range(6):
    for die_2 in range(6):
        if die_1 == die_2:
            counts[0] += 1
        else:
            counts[1] += 1
print(f'counts: triples {counts[0]:4d}   neither {counts[1]:4d}')
