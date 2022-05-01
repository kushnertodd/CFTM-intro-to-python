import sys

def exclude(a, b):
    good = True
    for c in a:
      if c in b:
        good = False
    return good

def get_vowels(a):
    vowels = ""
    for c in "aeiou":
        if c in a: 
            vowels += c
    return vowels

l = []
f = open("good-words.txt")
for line in f:
    trim = line.strip()
    #print(f'"{trim}"')
    l.append(trim)
f.close()
print(f'{l}')
trys = l.copy()
for w in l:
  trys.remove(w)
  #print(f'{w}: {trys}')
  for r in trys:
      if exclude(w, r):
        print(f'{w} {r} {get_vowels(w+r)}')
