from operator import itemgetter
from re import L




MAX_QSIZE = 10  
class CircleQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None]*MAX_QSIZE
    def isEmpty(self): return self.front==self.rear 
    def isFull(self): return self.front == (self.rear+1)*MAX_QSIZE
    def clear(self):self.front=self.rear

    def enqueue(self,item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    def size(self):
        return(self.rear-self.front+MAX_QSIZE)%MAX_QSIZE
    #원형큐 출력


# def display(self):
#         out=[]
#         if self.front < self.rear:
#             out = self.items[self.front+1:self.rear+1]
#         else:
#             out = self.items[self.front+1:MAX_QSIZE]\
#                 +self.items[0:self.rear+1]
#         print("[f=%s,r=%d] ==>"%(self.front,self.rear),out)
# items = [None,None,"B","C","D",None,None,None]
# q = CircleQueue()
# for i in range(8):q.enqueue(i)
# q.display()
# for i in range(5):q.dequeue();
# q.display()
# for i in range(8,14):q.enqueue(i)
# q.display()

#너비 우선 탐색 BFS

maze=[['1','1','1','1','1','1'],
      ['e','0','1','0','0','1'],
      ['1','0','0','0','1','1'],
      ['1','0','1','0','1','1'],
      ['1','0','1','0','0','x'],
      ['1','1','1','1','1','1']]
MAZE_SIZE=6

def isValid(x,y):
        if x<0 or y<0 or x>= MAZE_SIZE or y >= MAZE_SIZE:
            return False
        else:
            return maze[y][x] == '0' or maze[y][x] == 'x'
def BFS():
    que = CircleQueue()
    que.enqueue((0,1))
    print('BFS:')

    while not que.isEmpty():
        here =que.dequeue()
        print(here,end='->')
        x,y=here
        if(maze[y][x]=='x'):return True
        else:
            maze[y][x]='.'
            if isValid(x,y-1):que.enqueue((x,y-1))
            if isValid(x,y+1):que.enqueue((x,y+1))
            if isValid(x-1,y):que.enqueue((x-1,y))
            if isValid(x+1,y):que.enqueue((x+1,y))
result=BFS()
if result:print('-->미로탐색 성공')
else:print('-->미로탐색 실패')
