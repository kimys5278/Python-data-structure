#순차 탐색
def sequential_search(A,key,low,high):
    for i in range (low,high):
        if A[i].key == key :
            return i
    return None

# 이진 탐색 -  순환구조
def binary_search(A,key,low,high):
    if (low <=high):
        middle = (low+high)//2
        if key ==A[middle].key:
            return middle
        elif (key<A[middle].key):
            return binary_search(A,key,low,middle-1)
        else:
            return binary_search(A,key,middle+1,high)
    return None

#이진 탐색 - 반복구조
def binary_search(A,key,low,high):
    while(low <= high):
        middle = (low+high)//2
        if key == A[middle].key:
            return middle
        elif (key > A[middle].key):
            low = middle +1
        else:
            high = middle-1
    return None

# 보간 탐색
def binary_search(A,key,low,high):
    while(low <= high):
        middle = int (low+(high+low)*(key-A[low].key)/A[high].key-A[low].key)
        if key == A[middle].key:
            return middle
        elif (key > A[middle].key):
            low = middle +1
        else:
            high = middle-1
    return None

#탐색 키가 문자열인 경우
#문자를 아스키 코드로 변환하여 사용 ord()문자열을 아스키코드로 변환해주는 함수
def hash(key):
    sum=0
    for c in key:
        sum = sum +ord(c)
    return sum % M

class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def __str__(self):
        return str("%s:%s"%(self.key,self.value))
    #순차탐색 맵



class SequentialMap:
    def __init__(self):
        self.table=[]
    
    def size(self): return len(self.table)
    def display(self,msg):
        print(msg)
        for entry in self.table:
            print(" ", entry)
    def insert(self,key,value):
        self.table.append(Entry(key,value))

    def search(self,key):
        pos = sequential_search(self.table,key,0,self.size()-1)
        if pos is not None : return self.table[pos]
        else: return None
    
    def delete (self,key):
        for i in range(self.size()):
            if self.table[i].key == key:
                self.table.pop(i)
                return
map = SequentialMap()
map.insert('data','자료')
map.insert('structure','구조')
map.insert('sequential','선형 탐색')
map.insert('game','게임')
map.insert('binary','이진 탐색')
map.display("나의 단어장 :")

print("탐색:game -->",map.search('game'))
print("탐색:over -->",map.search('over'))
print("탐색:data -->",map.search('data'))

map.delete('game')
map.display('나의 단어장')

class Node:
    def __init__(self,elem,link=None):
        self.data=elem
        self.link=link

#체이닝을 이용한 해시 맵
class HashChainMap:
    def __init__(self,M):
        self.table = [None]*M
        self.M=M
    def hashFn(self,key):
        sum=0
        for c in key :
            sum = sum+ ord(c)
        return sum%self.M
    def insert(self,key,value):
        idx = self.hashFn(key)
        # self.table[idx] = None(Entry(key,value),self.table[idx])
        #위 코드가 복잡하면 풀어서 사용가능
        entry = Entry(key,value)
        node = Node(entry)
        node.link = self.table[idx]
        self.table[idx]=node
    
    def search(self,key):
        idx = self.hashFn(key)
        node = self.table[idx]
        while node is not None:
            if node.data.key == key :
                return node.data
            node = node.link
        return None
    
    def delete(self,key):
        idx = self.hashFn(key)
        node = self.table(idx)
        before = None
        while node is not None:
            if node.data.key == key :
                if before == None:
                    self.table[idx]=node.link
                else:
                    before.link = node.link
                return 
            before = node
            node = node.link
    
    def display(self,msg):
        print(msg)
        for idx in range(len(self.table)):
            node = self.table[idx]
            if node is not None:
                print("[%2d] -> "%idx,end=' -> ')
                node = node.link
            print()

d = {}
d['data']='자료'
d['structure']='구조'
d['sequential search']='선형 탐색'
d['game']='게임'
d['binary search']='이진 탐색'
print("나의 단어장")
print(d)

if d.get('game'):print("탐색:game-->",d['game'])
if d.get('over'):print("탐색:over-->",d['over'])
if d.get('data'):print("탐색:data-->",d['data'])

d.pop('game')
print("나의 단어장:")
print(d)







