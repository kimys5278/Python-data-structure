


class Stack:
    def __init__(self):
        self.top=[]
    def isEmpty(self):return len(self.top)==0
    def size(self):return len(self.top)
    def clear(self): self.top=[]

    def push(self,item):
        self.top.append(item)
    def pop (self):
        if not self.isEmpty():
             return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]        
    def __str__(self):
        return str(self.top)

    def __str__(self):
        return str(self.top[::1])

         
map=[['1','1','1','1','1','1'],
     ['e','0','0','0','0','1'],
     ['1','0','1','0','1','1'],
     ['1','1','1','0','0','x'],
     ['1','1','1','0','1','1'],
     ['1','1','1','1','1','1']]
MAZE_SIZE=6
def pos(x,y): 
        if x<0 or y<0 or x>= MAZE_SIZE or y >= MAZE_SIZE:
            return False
        else:
            return map[y][x] == '0' or map[y][x] == 'x' 
def DFS():
        s =Stack()
        s.push((0,1))
        print('DFS: ')

        while not s.isEmpty():
            here= s.pop()
            print(here,end=' ->')
            (x,y)=here
            if (map[y][x]=='x'):
                return True
            else:
                map[y][x]='.'
                if pos(x,y-1):s.push((x,y-1))
                if pos(x,y+1):s.push((x,y+1))
                if pos(x-1,y):s.push((x-1,y))
                if pos(x+1,y):s.push((x+1,y))
                print('현재스택',s)
            return False

result = DFS()
if result : print('--->미로탐색 성공')
else:print('--->미로탐색 실패')