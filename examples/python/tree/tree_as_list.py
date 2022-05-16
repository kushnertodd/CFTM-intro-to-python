"""
trees
  +----+-------+---+-----+-----+--------+   +-+-+-+-+-+-+
  |left|left_ct|key|value|right_ct|right| = |l|c|k|v|c|r|
  +----+-------+---+-----+-----+--------+   +-+-+-+-+-+-+

          +-+-+-+-+-+-+
          |l|1|B|b|r|1|
          +-+-+-+-+-+-+
            |       |
   +-+-+-+-+-+-+ +-+-+-+-+-+-+
   |l|0|A|a|r|0| |l|0|C|c|r|0|
   +-+-+-+-+-+-+ +-+-+-+-+-+-+

"""


def add_left(node, new):
    node['left'] = new
    node['left_ct'] += 1


def add_right(node, new):
    node['right'] = new
    node['right_ct'] += 1


def insert(node, key, value):
    if (key == node['key']):
        return
    elif (key > node['key']):
        if (node['right'] == None):
            add_right(node, new(key, value))
        else:
            insert(node['right'], key, value)
    elif (key < node['key']):
        if (node['left'] == None):
            node['left'] = new(key, value)
        else:
            add_left(node, new(key, value))


def new(key, value):
    return {'key': key, 'value': value, 'left': None, 'left_ct': 0, 'right': None, 'right_ct': 0}


def pr_node(node, name, suff=""):
    print(f'{name}: {node[name]}{suff}', end="")


def pr(node, d=0):
    print(f'{rep(" ", d)}', end="")
    pr_node(node, "key", ", ")
    pr_node(node, "value", ", ")
    pr_node(node, "left_ct", ", ")
    #pr_node(node, "left", ", ")
    pr_node(node, "right_ct")
    #pr_node(node, "right")
    print("")

def rep(c, n):
    s = ''
    for i in range(n):
        s += c
    return s


def walk(node, d=0):
    if node != None:
        pr(node, d)
        walk(node['left'], d + 2)
        walk(node['right'], d + 2)


top = new(3, 'v3')
#print(f'{top}')
walk(top)

print("")
insert(top, 5, 'v5')
#print(f'{top}')
walk(top, 0)

print("")
insert(top, 1, 'v1')
#print(f'{top}')
walk(top, 0)

print("")
insert(top, 7, 'v7')
#print(f'{top}')
walk(top, 0)
