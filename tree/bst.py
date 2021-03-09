 
import re

class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        #self.history = []
        self.count = 1
    
    def __str__(self):
        return 'Node(key={!r}, \nleft={!r}, \nright={!r})'.format(self.key, self.left, self.right)


def compareTo(this, that):
    assert type(this)==type(that), "Type of the two inputs must be the same!"
    if this>that:
        return 1
    if this<that:
        return -1
    return 0

class BST:
    '''
    binary search tree application
    input
    1. Insert: keys and values, take a space or comma as the separater   
    2. Floor: return the node of the current bst whose key <= the query key
    3. Ceiling: return the node of the current bst whose key >= the query key
    4. Delete minimum: delete minimum key
    '''
    def __init__(self, key, value):
        self.root = Node(key, value)

    def get(self, key):
        x = self.root
        while x != None:
            cmp = compareTo(key, x.key)
            if cmp<0: x = x.left
            elif cmp>0: x = x.right
            else: return x.value
        return None

    def put(self, key, value, x='root'):
        if x =='root':
            x = self.root
        if x is None:
            return Node(key, value)       
        cmp = compareTo(key, x.key)
        if cmp<0: x.left = self.put(key, value, x.left)
        elif cmp>0: x.right = self.put(key, value,x.right)
        else: x.value = value
        x.count = 1 + self.size(x.left) + self.size(x.right)
        return x

    def size(self, x):
        if x is None: return 0
        return x.count

    def traverse(self):
        q = []
        self.inorder(self.root, q)
        return q

    def inorder(self, x, queue):
        if x is None: return
        self.inorder(x.left, queue)
        queue.append(x.key)
        self.inorder(x.right, queue)
    
    def floor(self, key, x='root'):
        if x =='root':
            x = self.root
        if x is None:
            return None
        cmp = compareTo(key, x.key)
        if cmp==0: return x.key
        if cmp<0: return self.floor(key, x.left)
        t = self.floor(key, x.right)
        if t is not None:
            return t
        return x

    def ceiling(self, key, x='root'):
        if x =='root':
            x = self.root
        if x is None:
            return None
        cmp = compareTo(key, x.key)
        if cmp==0: return x.key
        if cmp>0: return self.ceiling(key, x.right)
        t = self.ceiling(key, x.left)
        if t is not None:
            return t
        return x
       

    def delete_min(self, x='root'):
        if x =='root':
            x = self.root
        if x.left is None:
            return x.right
        x.left = self.delete_min(x.left)
        x.count = 1 + self.size(x.left) + self.size(x.right)
        return x

    


if __name__=='__main__':
    key = input("Initialize BST with root key: ")
    value = input("Initialize BST with root value: ")
    bst = BST(key, value)
    while True:
        op = input("1. Insert\n2. Floor\n3. Ceiling\n4. Delete minimum\n")
        if op=='1':
            keys = re.split(r',|\s', input("Insert BST keys: "))
            values = re.split(r',|\s',input("Insert BST value: "))
            for key, value in zip(keys, values):
                bst.put(key, value)
        elif op=='2':
            key = input("Floor key:")
            print(bst.floor(key))
        elif op=='3':
            key = input("Ceiling key:")
            print(bst.ceiling(key))
        elif op=='4':
            print("Delete minimum")
            bst.root = bst.delete_min()
        print("Ordered bst ", bst.traverse())
        print("Size of bst: ", bst.size(bst.root))
        