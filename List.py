from re import A


a= [1,2,3]
print( str(a[2])+"hi")

a= [1,2,3]
a[2]= 4
print(a)

#del 삭제기능

a = [1,2,3,4,5]
del a[2:]
print(a)

#리스트에 요소추가 append
 
a = [1,2,3,4,5]
a.append(6)
print(a)

#리스트 정령 sort 
a = [1,9,4,5]
a.sort()
print(a)

a = ['a','c','d','b','e']
a.sort()
print(a)

# 역순으로 리스트 뒤집기 revrese
a1 = ['a','b','c']
a1.reverse()
print(a1)

# 위치반환 index
a = [1,2,3]
print(a.index(3),a.index(1))

#리스트에 요소삽입 insert

a = [1,2,3]
a.insert(0,9)
print(a)

#리스트 요소제거
#3두개인데 a.remove(3)을 하면 앞 3 만 없어짐. 두개의 3을 제거하려면 a.remove(3)함수를 두번 사용하면된다.

a = [1,2,3,4,5,1,2,3]
a.remove(3)
a.remove(3)
print(a)

#요소끄집어내기
#pop()은 리스트 맨마지막 요소를 돌려주고 그 요소는 삭제

a = [1,2,3]
a.pop()
print(a)

# pop(1)안에 숫자를 넣으면 a[1]의값을 돌려주고, 삭제

a = [1,2,3]
a.pop(0)
print(a)

#리스트 확장 extned
a = [1,2,3]
a.extend([4,5])
b = [6,7,8]
a.extend(b)
print(a)


A= [1, 6, 9]
B =[2, 7, 8]

A.extend(B)
print(A)

a = [1,2,3]



def delete ():
    return a.pop(0)
print(a)