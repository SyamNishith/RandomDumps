'''class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def Traversal(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_last(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print("Linkedlist is empty")
        elif self.head.ref is None:
            new_node.ref=self.head
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
                print("node not found")
            else:
                new_node.ref=n.ref
                n.ref=new_node
    def add_after(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print("Linkedlist is empty")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.ref
            if n.data is None:
                print("node is not found")
            else:
                new_node.ref=n.ref
                n.ref=new_node
    def delete_node(self,x):
        if self.head is None:
            print("linked list is empty cannot perform deletion operation")
        else:
            n=self.head
            if n.data==x:#for first node
                self.head=self.head.ref
            else:#for any node
                while n.ref is not None:
                    if n.ref.data==x:
                        break
                    n=n.ref
                if n.ref.data is None:
                    print("Node not found")
                else:
                    n.ref=n.ref.ref
ll=Linkedlist()
ll.add_begin(5)
ll.add_last(10)
ll.add_last(15)
ll.add_before(7,10)
ll.add_after(17,15)
ll.add_after(18,17)
ll.delete_node(17)
ll.Traversal()'''
'''from itertools import combinations
def string_pairs(string):
    for ch in string:
        print(ch,end=" ")
    print()
    for pairs in range(2,len(string)+1):
        for c in combinations(string,pairs):
            print("".join(c),end=" ")
        print()
string="ram"
string_pairs(string)'''
'''def calculate_lcm(n,m):
    if n>m:
        high=n
    else:
        high=m
    max=high
    while True:
        if high%n==0 and high%m==0:
            print("lcm is:",high)
            break
        else:
            high=high+max
m,n=map(int,input("enter the values:").split())
calculate_lcm(m,n)'''
'''def computegcd(n,m):
    if m==0:
        return n
    else:
        return computegcd(m,n%m)
m,n=map(int,input("enter the values:").split())
print(computegcd(n,m))'''
'''number=int(input("enter the number:"))
my_list=[]
while number:
    my_list.append(number%10)
    number=number//10
my_list.sort()
print(my_list)
freq={}
for num in my_list:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for i,j in freq.items():
    print(f"the digit {i} occurs {j} times")'''
'''num=1212121
s=str(num)
se=set(s)
for i in se:
    print(f"the digit {i} occurs {s.count(i)} times")'''
'''a="h-e-l-l-o"
b=a.split('-')
print(b)
c="".join(b)
print(c)'''
'''n=int(input("enter the range of fibobacci series:"))
a,b=0,1
print(a,end=" ")
print(b,end=" ")
for i in range(2,n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c'''
'''amount=int(input("enter the amount:"))#1000
total=amount//500
print(f"500 notes are-->{total}")
amount=amount-(total*500)
total=amount//200
print(f"200 notes are-->{total}")
amount=amount-(total*200)
total=amount//100
print(f"100 notes are-->{total}")
amount=amount-(total*100)
total=amount//50
print(f"50 notes are-->{total}")
amount=amount-(total*50)
total=amount//20
print(f"20 notes are-->{total}")
amount=amount-(total*20)
total=amount//10
print(f"10 notes are-->{total}")
amount=amount-(total*10)
total=amount//5
print(f"5 notes are-->{total}")
amount=amount-(total*5)
total=amount//2
print(f"2 notes are-->{total}")
amount=amount-(total*2)
total=amount//1
print(f"1 notes are-->{total}")'''
'''from itertools import combinations
s="syam"
for i in s:
    print(i,end=" ")
for ch in range(2,len(s)+1):
    for j in combinations(s,ch):
        print("".join(j),end=' ')'''
'''n=int(input("enter the number of rows:"))
for i in range(n):
    k=ord("A")+i
    for j in range(i+1):
        print(chr(k),end="  ")
        k=k+1
    print()'''
'''def hello(number):
    width = len(bin(n)[2:])
    for i in range(1,n+1):
        deci=str(i)
        octa=oct(i)[2:]
        hexa=hex(i)[2:].upper()
        bina=bin(i)[2:]
print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width),end=" ")'''
'''def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)'''
'''x,y,z,n=map(int,input("enter the values:").split())
my_list=[[i,j,k]for i in range(x+1)for j in range(y+1)for k in range(z+1) if i+j+k!=n]
print(my_list)'''
'''name,*scores=input("enter the values:").split()
print(name)
print(scores)'''
'''n=int(input())
print(n+(n*60/100))'''
n=int(input("enter the units:"))
if n>0 and n<=50:
    cost=(n*0.50)
elif n>50 and n<=99:
    cost=((n*1)-25)
elif n>99 and n<=200:
    cost=((n*1.5)-74)
elif n>200:
    cost=((n*2)-226)
print(round(cost))






















































