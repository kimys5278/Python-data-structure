


from 자료구조스택 import isEmpty


class Node:
    def __init__(self,elem,link=None):
        self.data=elem
        self.link=link
#연결된 스택
class LinkStack:
    def __init__(self):
        self.top=None

    def isEmpty(self):
        return self.top==None

    def clear(self):
        self.top=None

    def push(self,item):
        n=Node(item,self.top)
        self.top=n
    
    def pop(self):
        if not self.isEmpty():
            n=self.top
            self.top=n.link
            return n.data
    
    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def size(self):
        node =self.top
        count =0
        while not node == None:
            node = node.link
            count+=1
        return count 

    def display(self,msg='LinkStack'):
        print(msg,end='')
        node=self.top
        while not node==None:
            print(node.data,end='')
            node=node.link
        print()
    def test(self):
        p=list
        while self.node != None:
            print(self.node.data,end=' ')
            self.node=self.node.link 
    def reverseList(self, head):
        self.node = None
        while head:
            temp = head
            head = head. next
            temp . next = prev
            prev = temp
        return prev
    def display_reserve(self,msg = 'reserve :'):
        
        p = self.size()-1
        while p >=0:
            node = self.getNode(p)
            print(node.data,end=' ')
            p-=1



odd = LinkStack()
even = LinkStack()
for i in range(10):
    if i%2==0: even.push(i)
    else:odd.push(i)
print('스택 even push 5 회',even.push)
print('스택 odd push 5 회',odd.push)
print('스택 even     peek',even.peek())
print('스택 even     peek',odd.peek())
for i in range(2):even.pop()
for i in range(3):odd.pop()
print('스택 even pop 2회',even.pop())
print('스택 even pop 3회',odd.pop())

#연결된 리스트
class LinkStack:
    def __init__(self):
        self.head=None
    def isEmpty(self):return self.head  == None
    def clear(self):self.head=None
    def size(self):
        node=self.top
        count=0
        while not node ==None:
            node = node.link
            count+=1
        return count
    
    def display(self,msg='LinkStack'):
        print(msg,end='')
        node=self.head
        while not node == None:
            print(node.data,end='')
            node=node.link
        print()

    def getNode(self,pos):
        if pos<0 : return None
        node = self.head
        while pos>0 or node !=None:
            node = node.link
            pos-=1
        return node

    def getEntry(self,pos):
        node = self.getNode(pos)
        if node == None:return None
        else: return node.data

    def replace (self,pos,elem):
        node = self.getNode(pos)
        if node !=None:node.data = elem 

    def find(self,data):
        node=self.head
        while node is not None:
            if node.data==data:return node
            node = node.link
        return None

    def insert(self,pos,elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem,self.head)
        else:
            node=Node(elem,before.link)
            before.link = node
    
    def delete(self,pos):
        before = self.getNode(pos-1)
        if before == None:
            self.head=self.head.link
        elif before.link != None:
            before.link = before.link.link

s=LinkStack()
s.display('단순연결리스트 초기상태 : ')
s.insert(0,10); s.insert(0,20); s.insert(1,30); s.insert(3,40); s.insert(2,50)
s.display('단순연결리스트 삽입 x5 : ')
s.replace(2,90)
s.display('단순연결리스트 교체 : ')
s.delete(2); s.delete(3); s.delete(0)
s.display('단순연결리스트 삭제x3 : ')
s.display()
s.clear()
s.display('단순연결리스트 초기화 : ')            

#원형 연결리스트

class CircleLinkedQueue:
    def __init__(self):
        self.tail=None
    def isEmpty(self):
        return self.tail==None
    def clear(self):
        self.tail=None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
    def enqueue(self,item):
        node=Node(item,None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link=self.tail.link
            self.tail=node
    def dequeue(self):
        if not isEmpty():
            data=self.tail.link.data
            if self.tail.link==self.tail:
                self.tail=None
            else:
                self.tail.link=self.tail.link.link
            return data
    def size(self):
        if self.isEmpty(): return 0
        else:
            count=1
            node=self.tail.link
            while not node == self.tail:
                node=node.link
                count+=1
            return count
    def display(self,msg='CircleLinkedQueue'):
        print(msg,end='')
        if not isEmpty():
            node=self.tail.link
            while not node==self.tail:
                print(node.data,end='')
                node=node.link
            print(node.data,end='')
        print()
q=CircleLinkedQueue()

n=CircleLinkedQueue()
while n==-1:
    n=input("양의정수입력 -1종료")
n.display()