import random
counts = [0, 0, 0]
for d1 in range(6):
    for d2 in range(6):
        for d3 in range(6):
            die_1 = d1
            die_2 = d2
            die_3 = d3
            # roll three dice by creating three arbitrary numbers between one and 6
            #die_1 = random.randint(1, 6)
            #die_2 = random.randint(1, 6)
            #die_3 = random.randint(1, 6)# check for all dice having the same value
            #print(f'dice: {die_1:2d} {die_2:2d} {die_3:2d}   ', end='')
            if die_1 == die_2 and die_2 == die_3: 
                #print("three with the same value: ", die_1)
                counts[0] += 1
            else:
                # exchange the second and third if the second is greater than the third
                if die_1 > die_2: 
                    temporary_value = die_2
                    die_2 = die_1
                    die_1 = temporary_value
                # exchange the second and third if the second is greater than the third
                if die_2 > die_3: 
                    temporary_value = die_3
                    die_3 = die_2
                    die_2 = temporary_value
                # exchange the second and third if the second is greater than the third
                if die_1 > die_2: 
                    temporary_value = die_2
                    die_2 = die_1
                    die_1 = temporary_value
                # check for all three values successive in a sequence
                if die_1+1 == die_2 and die_2+1 == die_3: 
                    #print("three in a row:            ", die_1, die_2, die_3)
                    counts[1] += 1
                else:
                    #print("no triples or sequence:    ", die_1, die_2, die_3)
                    counts[2] += 1
print(f'counts: triples {counts[0]:4d}   sequence {counts[1]:4d}   neither {counts[2]:4d}')
