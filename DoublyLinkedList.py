class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class DoublyLinledLisi:
    def __init__(self):
        self.head=None
    def frwd_traverse(self):
        if self.head is None:
            print("DoublyLinedList is Empty:")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.nref
    def bkwd_traverse(self):
        print()
        if self.head is None:
            print("doublyLinkedList is Empty:")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.pref
    def insert_empty(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            print("DoublyLinkedList Is Not Empty:")
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def add_last(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    def add_after(self,data,x):
        if self.head is None:
            print("DoublyLinkedList is Empty:")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("node is not found:")
            else:
                new_node=Node(data)
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node
    def add_before(self,data,x):
        if self.head is None:
            print("DoublyLinkedList is Empty:")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("node is not found:")
            else:
                new_node=Node(data)
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                n.pref=new_node
    def delete_begin(self):
        if self.head is None:
            print("DoublyLikedList is empty,cannot perform delete operation:")
            return
        if self.head.nref is None:
            self.head=None
            print("DoublyLinkedList is empty after deleting the node:")
        else:
            self.head=self.head.nref
            self.head.pref=None
    def delete_end(self):
        if self.head is None:
            print("cannot delete node")
            return
        if self.head.nref is None:
            self.head=None
            print("DoublyLinkedList is empty after deleting node")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
    def delete_by_value(self,x):
        if self.head is None:
            print("DLL is empty cannot perform delete operation")
            return
        if self.head.nref is None:
            if self.head.data==x:
                self.head=None
            else:
                print("x is not present in DLL")
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref
        if n.nref is not None:
            n.pref.nref=n.nref
            n.nref.pref=n.pref
        else:
            if x==n.data:
                n.pref.nref=None
            else:
                print("x is not present in  doubly linked list")
DLL=DoublyLinledLisi()
DLL.add_begin(9)
DLL.add_last(10)
DLL.add_after(56,10)
DLL.add_before(55,56)
DLL.delete_by_value(10)
DLL.frwd_traverse()
            