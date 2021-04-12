# 반복문: while
# 조건이 맞을때 계속 실행
#
# while True:
#     print("python")
#
# a = 0
# while True:
#     a += 1 # a = a + 1
#     if a > 10:
#         break
#     print(a)
#
# a = 0
# while a < 10:
#     a += 1
#     print(a)
#
# 실습) 1~10까지 합을 출력
#
# s = 0 # 합계를 누적 할 변수
# x = 0 # 증강 할 변수
# while True:
#     x += 1
#     if x > 10:
#         break
#     s += x
# print(s)
#
# a가 증가하면서 합계를 구하고 그 합계가 2000이 넘으면 종료
#
# 방법1)
#
# s = 0 # 합계 누적 변수
# a = 0 # 증가 변수
# while True:
#     a += 1
#     s += a
#     if s>2000:
#         print(a, s)
#         break
#
# 방법2)
#
# s = 0
# a = 0
#
# while s < 2000:
#     a += 1
#     s += a
# print("a--> 값",a, "s--> 값",s)
#
#
# 사용자가 입력 한 수를 누적 하다가 만약
# 0을 입력하면 반복문 누적 합계를 출력
#
#방법1)

# s = 0
#
# while True:
#     a = int(input("수를 입력해주세요."))
#     if a == 0:
#         break
#     s += a
# print(s)
#
# 방법2)
#
# s = 0
# a = 1
# while a != 0:
#     a = int(input("수를 입력해주세요."))
#     s += a
# print(s)
