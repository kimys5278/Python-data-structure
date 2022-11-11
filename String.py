# 문자열
a = "Hello world"

print(a)

# 문자열 자료형
a = "Python's is good"
b = 'Python\'s is good'  # '' 안에 또 '있다면 오류 그래서 \' 로 해주면문자열로 인식

print(a)
print(b)

# 이스케이프 코드

# \n - 문자열 안에서 줄바꿈
# \t - 문자열 사이에 탭 간격을 줄 때사용
# \\ - 문자 \ 를 그대로 표현할 때 사용
# \' - 작은 따옴표 ' 를 그대로 사용
# \" - 큰 따옴표 " 를 그대로 사용
c =  "My name is Yu seong. \n My favorite color is balck."
print(c)


# """  문장  """ 을 쓰면 이스케이프 코드 안쓰고 적는대로 출려됨
c =  """My name is Yu seong. 

My favorite color is balck."""
print(c)

# 문자열 더하기 ,곱하기

a = "hello"
b = "world"

print(a+b)
print(a*3)

# 인덱싱

a = "Life is too short, You need Python"
print(a[5])
print(a[-1])

#슬라이싱
     
# a [이상 : 미만 : 간격 ]

a = "201904197"

print(a[:5:2])
print(a[:5:-2])

# 문자열 포맷팅
# (한개)
a = " I eat %d three apples" % 3

print(a)

#  (여러개)  # %s 는 숫자나 여러가지 문자를 그냥 문자열로 나타내기 때문에 %s 는 다됨. 편함
number = 10
day = 15
a = "I ate  %d apples. so i sick for %s days"%(number,day)
print(a)

q= " My name is {name}, {age} .".format(name="유성", age = 23)
print(q) 
 
 # 앞에 f 만 붙혀도됨
name = int 
a= f"나의 이름은 {name}"
print(a)

# 공백
a = "%10s " % "hi"
print(a)

a = "%f"%3.1454865 
print(a) 

# 실수 소수점 자르기
a = "%0.4f"%3.1454865  #0.4f 중에서 0은 간격 4 는 남길 소수점 
print(a) 

# 문자열 개수 세기
a = "hobby"
print(a.count('b'))  # 문자에서 b 의 갯수 찾기

a = "hoibby"
print(a.find('b')) # 문자에서 b 가 몇번쨰에 나오는지 출력. 물론 맨 앞에 있는 b. 두번째 b 는 안걸림
print(a.find('c')) # 아무것도 없으면 -1 출력

#join 함수
a = ",".join("abcde")
print(a)

#대소문자 바꾸기
a = "hi"
print(a.upper())

b = "HI"
print(a.lower())

# 공백없애기
a = "         hi         "
print(a.strip())

# 문자열 교체하기
a = "Life is good"
print(a.replace("Life","Food"))

# Split함수 # 띄어쓰기를 기점으로 리스트형으로 만듬
a = "Life is good"
print(a.split())