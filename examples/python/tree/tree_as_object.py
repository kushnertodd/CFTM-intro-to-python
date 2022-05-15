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


def rep(c, n):
    s = ''
    for i in range(n):
        s += c
    return s


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.left_ct = 0
        self.right = None
        self.right_ct = 0

    def add_left(self, new):
        self.left = new
        self.left_ct += 1

    def add_right(self, new):
        self.right = new
        self.right_ct += 1

    def insert(self, key, value):
        if (key == self.key):
            return
        elif (key > self.key):
            if self.right is None:
                self.add_right(Node(key, value))
            else:
                self.right.insert(key, value)
        elif (key < self.key):
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.add_left(Node(key, value))

    def pr(self, d=0):
        print(f'{rep(" ", d)}', end="")
        print(f'key: {self.key}, ', end="")
        print(f'value: {self.value}, ', end="")
        print(f'left_ct: {self.left_ct}, ', end="")
        print(f'right_ct: {self.right_ct}')

    def walk(self, d=0):
        self.pr(d)
        if self.left:
            self.left.walk(d + 2)
        if self.right:
            self.right.walk(d + 2)


top = Node(3, 'v3')
top.walk()

print("")
top.insert(5, 'v5')
top.walk(0)

print("")
top.insert(1, 'v1')
top.walk()

print("")
top.insert(7, 'v7')
top.walk()
