class BinarySearchTree:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BinarySearchTree(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BinarySearchTree(data)
    def search(self,data):
        if self.key==data:
            print("Node is found in the tree:")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in the tree:")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in the tree:")
    def preorder_traversal(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder_traversal()
        if self.rchild:
            self.rchild.preorder_traversal()
    def inorder_traversal(self):
        if self.lchild:
            self.lchild.inorder_traversal()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder_traversal()
    def postorder_traversal(self):
        if self.lchild:
            self.lchild.postorder_traversal()
        if self.rchild:
            self.rchild.postorder_traversal()
        print(self.key,end=" ")
    def deletion(self,data):
        if self.key is None:
            print("tree is empty cannot perform deletion operation")
            return
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.deletion(data)
            else:
                print("node is not present in the tree:")
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.deletion(data)
            else:
                print("node is not present in the tree:")
        else:
            if self.lchild is None: #for node with single child node
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None: #for node with single child node
                temp=self.lchild
                self=None
                return temp
            node=self.rchild #for node with two child nodes
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.deletion(node.key)
        return self
    def min_node(self):
        current=self
        while current.lchild:
            current=current.lchild
        print("minimum node in the tree is:",current.key)
    def max_node(self):
        current=self
        while current.rchild:
            current=current.rchild
        print("maximum node in the tree is:",current.key)
root =BinarySearchTree(1)
list=[10,23,31,4,11,18,56,98]
for i in list:
    root.insert(i)
print("preorder:")
root.preorder_traversal()
print()
print("Inorder:")
root.inorder_traversal()
print()
print("postorder:")
root.postorder_traversal()
print()
root.search(56)
root.max_node()
root.min_node()