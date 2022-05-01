import sys


def swap(list, i, j):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp


def sort(list):
    print(f'sort({list} lenth {len(list)}')
    list_length = len(list)
    for i in range(list_length - 1):
        sublist_length = list_length - i - 1
        print(f'sort comparing from list[{sublist_length}] = {list[sublist_length]} up to list[{i}] = {list[i]}')
        for j in range(sublist_length):
            compare_index = list_length - j - 1
            current = list[compare_index]
            above = list[compare_index - 1]
            print(f'    {compare_index}: comparing list[{compare_index}] = {current} to list[{compare_index - 1}] = {above}')
            if current > above:
                print(f'            swap list[{compare_index}] = {current} to list[{compare_index - 1}] = {above}')
                swap(list, compare_index, compare_index - 1)
            print(f'    list {list}')


def to_int(arg):
    try:
        return int(arg)
    except ValueError:
        print(f'{arg} is not an integer')
        exit(0)


def to_real(arg):
    try:
        return float(arg)
    except ValueError:
        print(f'{arg} is not a real number')
        exit(0)


list = []
if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} no ...')
else:
    for i in range(len(sys.argv) - 1):
        no = sys.argv[i + 1]
        #print(f'list[{i}] = {sys.argv[i + 1]}')
        list.append(no)
    sort(list)
    print(f'final: {list}')
