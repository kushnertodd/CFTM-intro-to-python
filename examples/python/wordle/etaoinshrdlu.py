import sys
if len(sys.argv) < 2:
    print(f'{sys.argv[0]} word')
    exit(0)
letters = sys.argv[1]
good = True
#print(f'checking "{letters}"')
for c in letters:
    if not c in 'etaoinshrdlu':
        good = False
    #print(f'    checking {c} "{letters}" = {good}')
if good:
    print(letters)
