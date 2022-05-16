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

# get all permutations of letters
def chars_permutations(letters, length):
    letters_length = len(letters)
    if (letters_length < length):
        error(f'fewer than {letters_length} letters: {letters}')
    letter_list = split(letters)
    perm_list = permutations(letter_list, length)
    result = []
    for perm in perm_list:
        result.append("".join(perm))
    return result

# debug output
def debug(message):
    if debugging:
        print(message)

# print error message and exit
def error(message):
    print(message)
    exit(0)

# get all permutations of the given length from list
def permutations(list, length):
    if (length == 0):
        result = [[]]
        return result
    result = []
    for item in list:
        rest = list[:]
        rest.remove(item)
        rest_permutations = permutations(rest, length-1)
        item_rest_permutations = prepend(item, rest_permutations)
        result += item_rest_permutations
    return result

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

# create all 5 char permutations of letters
permchars = chars_permutations(letters, length)
#print (f'{permchars}')
for perm in permchars:
    print(perm)

