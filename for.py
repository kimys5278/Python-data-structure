import numbers
from tokenize import Number


test_list=['one','two','three']
for i in test_list:
    print(i)

a = [(1,2),(3,4),(5,6)]
for (first , last) in a:
    print(first , last)

# num = [90,80,75,60,80]
# number = 0

# for nums in num:
#     number = number +1
#     if nums >= 60:
#         print("%d번 학생은 합격입니다."%number)
#     else:
#         print("%번 학생은 불합격입니다."%number)

# point=[90,80,70,60,50]
# number = 0

# for points in point:
#     number = number+1
#     if points >= 90:
#         print("%d번 학생의 점수는 90점이므로 A입니다."%number)
#     elif points >= 80:
#         print("%d번 학생의 점수는 80점이므로 B입니다."%number)
#     elif points >= 70:
#         print("%d번 학생의 점수는 70이므로 c입니다."%number)
#     elif points >= 60:
#         print("%d번 학생의 점수는 60이므로 d입니다."%number)
#     else:
#         print("%d번 학생의 점수는 50이므로 f입니다."%number)

    #continue
    marks = [90,80,70,60,50]

    number = 0
    for mark in marks:
         number = number+1

    if mark >= 60: continue
    print("%d번 학생은 합격입니다."%number)