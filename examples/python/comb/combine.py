import re
import sys

'''
program to compute all possible 5 letter words that can be made for a set of letters
usage:
  py wordle.py letters
'''

debugging = 0

# return item.list
def cons(item, list):
    temp = list[:]
    temp.insert(0, item)
    return temp

# get all combinations of letters
def chars_combinations(letters, length):
    letters_length = len(letters)
    if (letters_length < length):
        error(f'fewer than {letters_length} letters: {letters}')
    letter_list = split(letters)
    comb_list = combinations(letter_list, length)
    result = []
    for comb in comb_list:
        result.append("".join(comb))
    return result

# get all combinations of the given length from list
def combinations(list, length):
    if (length == 0):
        result = [[]]
        return result
    if (len(list) == length):
        result = [list[:]]
        return result
    result = []
    rest = list[:]
    first = rest.pop(0)
    combs1 = combinations(rest, length-1)
    prepend1 = prepend(first, combs1)
    result += prepend1
    combs2 = combinations(rest, length)
    result += combs2
    return result

# debug output
def debug(message):
    if debugging:
        print(message)

# print error message and exit
def error(message):
    print(message)
    exit(0)

# return [i.sublist i.sublist...]
def prepend(item, list):
    result = []
    for sublist in list:
        result = cons(cons(item, sublist), result)
    return result

# split word into a list of individual characters
def split(word):
    return [char for char in word]

def usage(program):
    error(f'usage: {program} letters length')

# main
if len(sys.argv) < 3:
    usage(sys.argv[0])

letters = sys.argv[1]
length = int(sys.argv[2])

# load all 5 letter words
f = open("dict5.txt")
words5chars = {}
for l in f:
    s = l.strip()
    # just note that word exists, use dict for efficient lookup
    words5chars[s] = True
f.close()

# create all 5 char combinations of letters
combchars = chars_combinations(letters, length)
#print (f'{combchars}')
for comb in combchars:
    print(comb)

