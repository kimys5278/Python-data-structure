def factorial (n):
    if n ==1 :return 1
    else : return n * factorial(n-1)  
    
print(factorial(4))

#재귀함수 예시
def aFunc():
    print("호출!")
    aFunc() #자신을 호출

##메인 코드
aFunc()