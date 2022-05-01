import sys


def listoff(i, l):
    l.remove(i)


print("ref test")
a = [1, 2, 3]
print(f'before: {a}')
listoff(2, a)
print(f'after: {a}')

print("val test")
a = [1, 2, 3]
print(f'before: {a}')
listoff(2, a[:])
print(f'after: {a}')
