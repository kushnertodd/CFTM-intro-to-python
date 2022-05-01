import random

counts = [0, 0, 0]
for d1 in range(6):
    for d2 in range(6):
        die_1 = d1
        die_2 = d2
        if die_1 == die_2:
            counts[0] += 1
        else:
            # exchange the second and third if the second is greater than the third
            if die_1 > die_2:
                temporary_value = die_2
                die_2 = die_1
                die_1 = temporary_value
            # check for all three values successive in a sequence
            if die_1 + 1 == die_2:
                counts[1] += 1
            else:
                counts[2] += 1
print(f'counts: triples {counts[0]:4d}   sequence {counts[1]:4d}   neither {counts[2]:4d}')
