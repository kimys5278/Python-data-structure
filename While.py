#while문
treehit = 0
while treehit < 10:
    treehit += 1
    print("나무를 %d번 찍었다."%treehit)
    if treehit == 10 :
        print("나무가 넘어갔습니다. 완료")

cake = 10
money = 8000
while money:
    print("돈을 받았으니 케이크를 드릴게요")
    cake -= 1
    print("케이크가 %d개 남았습니다"%cake)
    if not cake:  # cake == 0: 이렇게 해도됨.
        print( "케이크가 다 팔렸습니다.")
        break

#continue - while 문을 수행하다가 continue를 만나면 다시 while문 처음으로 돌아온다. 조건에 성립하지 않으면 출력. 

a = 0
while a<10:
    a +=1
    if a%2 ==0:
        continue
    print(a)

#무한루프- True면 무한적으로 실행됨 ctrl+c 하면 중지
while True:
     print("안녕")




