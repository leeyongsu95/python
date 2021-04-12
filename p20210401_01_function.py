# 내장함수
# data = [9, 8, 7, 6]
# print(sum(data))
#
# 사용자 함수 sum 정의:
# 매개변수 : 리스트, 반환 값: 합계
#
# def mysum(a):  # def = 정의한다.
#     s = 0
#     for x in data:
#         s += x
#     # print(s)
#     return s
#
# data = [18, 8, 7, 6]
#
# r = mysum(data)
#
# print("리턴 값:", r)
#
#
#
# max 함수: 리스트 중에 가장 큰 값을 저장.
# min 함수: 리스트 중 가장 작은 값을 저장.
#
# ys = [100, 20, 15, 60]
# u = max(ys)
#
# print("가장 큰 값", u)
#
# m = min(ys)
#
# print("가장 작은 값", m)
#
# max 가장 높은 값  사용자 함수
#
# def mymax(ys):
#     mx = ys[0]
#     for x in ys:
#         if x > mx:
#             mx = x
#     return mx
#
# ys = [100, 1, 15, 60]
# my = max(ys)
# print("가장 큰 값",my)
#
#
# min 가장 작은 값 사용자 함수
#
# def maxm(ls):
#     mx =ls[0]
#     for x in ls:
#         if x > mx:
#             mx = x
#     return mx
#
# # 전역변수
# ls = input("수를 입력하세요.").split(",")
# m = min(ls)
# print("가장 작은 값", m)
#
# 같이 푼 방법)
# min값을 구하는 함수
# def mymin(mindata):
#     mi = mindata[0]
#     for x in mindata:
#         if x < mi:
#             mi = x
#     return mi
#
# data = [78, 8, 5, 16]
# result =mymin(data)
# print('가장작은값:', result)
#
# ord() 함수
# 한글은 유니코드 체계
# print(ord("A"), len("A"), "A".encode(), len("A".encode()))
# print(ord("가"), len("가"), "가".encode(), len("가".encode()))
#
# print(chr(44032))
#
# 실습) 사칙연산 함수 구현
# 매개변수 : 두수, 반환 값 : 결과
#
# def add(a, b):
#     return a + b
#
# def abb(a, b):
#     return a - b
#
# def cal(a, b):
#     return a+b, a-b
#
# print("더하기", add(10, 20))
# print("빼기", abb(10, 50))
# print("빼기", cal(10, 20)[0], cal(10, 20)[1])
#
# 실습) 월급 구하기
# 년봉, 시급, 초과 근무 시간을 매개변수로 받아
# 월급을 계산하고 반환하는 함수
# (월급 = 년봉 / 12 + 시급 * 초과 근무시간)
#
# 내가 한 방법)
#
# def moy(sa, ho, ti):
#     return sa / 12 + ho * ti
#
# salary = int(input("당신의 연봉은?"))
# print(salary)
# hourly = int(input("당신의 시급은?"))
# print(hourly)
# time = int(input("초과 근무 시간은?"))
# print(time)
# print("월급:", moy(salary, hourly, time))
#
#
#
# 같이 푼 방법)
#
# def money(ys, ts, os):
#     return ys / 12 + ts * os
#
# yearS = 30000000 # 연봉
# timeS = 20000    # 시급
# overS = 1        # 초과 근무시간
# print("월급:", money(yearS, timeS, overS))
