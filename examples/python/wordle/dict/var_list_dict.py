def var(v, val):
  v = val

def dict(d, k, val):
  d[k] = val

def list(l, n, val):
  l[n] = val

print("test setting var, dict, list in function")
n = 2
print(f'var  n before            {n}')
var(n, 3)
print(f'     n after n = 3:      {n}')

d = {'i': 5, 'j': 6}
print(f'dict d before            {d}')
dict(d, 'i', 7)
print(f'     d after d[\'i\'] = 7: {d}')

l = [8, 9]
print(f'list l before            {l}')
list(l, 0, 10)
print(f'     l after l[0] = 10:  {l}')

