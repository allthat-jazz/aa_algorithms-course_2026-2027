class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.height = 1

def height(v): return v.height if v else 0
def update(v): v.height = max(height(v.left), height(v.right)) + 1
def balance(v): return height(v.right) - height(v.left)

def rotate_left(a):
    b = a.right
    a.right = b.left
    b.left = a
    update(a); update(b)
    return b

def rotate_right(a):
    b = a.left
    a.left = b.right
    b.right = a
    update(a); update(b)
    return b

def rebalance(v):
    update(v)
    if balance(v) == 2:
        if balance(v.right) < 0: v.right = rotate_right(v.right)
        return rotate_left(v)
    if balance(v) == -2:
        if balance(v.left) > 0: v.left = rotate_left(v.left)
        return rotate_right(v)
    return v

def insert(v, x):
    if not v: return Node(x)
    if x < v.key: v.left = insert(v.left, x)
    elif x > v.key: v.right = insert(v.right, x)
    else: return v
    return rebalance(v)

def remove(v, x):
    if not v: return None
    if x < v.key: v.left = remove(v.left, x)
    elif x > v.key: v.right = remove(v.right, x)
    else:
        if not v.left or not v.right: return v.left or v.right
        m = v.right
        while m.left: m = m.left
        v.key = m.key
        v.right = remove(v.right, m.key)
    return rebalance(v)

def next_key(v, x):
    result = None
    while v:
        if v.key == x: return x
        if v.key > x: result = v.key; v = v.left
        else: v = v.right
    return result

def prev_key(v, x):
    result = None
    while v:
        if v.key == x: return x
        if v.key < x: result = v.key; v = v.right
        else: v = v.left
    return result

def preorder(v, keys):
    if v:
        keys.append(str(v.key))
        preorder(v.left, keys)
        preorder(v.right, keys)

root = None
out = []
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'add': root = insert(root, int(cmd[1]))
    elif cmd[0] == 'del': root = remove(root, int(cmd[1]))
    elif cmd[0] == 'exists':
        x = int(cmd[1])
        out.append('YES' if next_key(root, x) == x else 'NO')
    elif cmd[0] == 'next': out.append(str(next_key(root, int(cmd[1]))))
    elif cmd[0] == 'prev': out.append(str(prev_key(root, int(cmd[1]))))
    elif cmd[0] == 'root': out.append(str(root.key) if root else 'Empty')
    elif cmd[0] == 'height': out.append(str(height(root)))
    elif cmd[0] == 'print':
        keys = []
        preorder(root, keys)
        out.append(' '.join(keys) if keys else 'Empty')
print('\n'.join(out))
