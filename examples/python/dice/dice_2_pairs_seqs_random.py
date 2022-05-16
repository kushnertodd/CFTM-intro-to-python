import random
# roll two dice by creating three arbitrary numbers between one and 6
die_1 = random.randint(1, 6)
die_2 = random.randint(1, 6)
print("The two dice are: ", die_1, die_2)
if die_1 == die_2:
    print("Both dice have the same value: ", die_1)
else:
    # exchange the first and second if the first is greater than the second
    if die_1 > die_2:
        temporary_value = die_2
        die_2 = die_1
        die_1 = temporary_value
    # check for all three values successive in a sequence
    if die_1 == die_2+1:
        print("Both dice are a sequence: ", die_1, die_2)
    else:
        print("The dice are different and not in sequence: ", die_1, die_2)
