# 연습문제 실습 1)
#
#
# 1) 별 찍기 1
#
#
# print('☆' * 1)
# print('☆' * 2)
# print('☆' * 3)
# print('☆' * 4)
# print('☆' * 5)
# print('☆' * 6)
#
#
# for x in range(1, 7): # 시작점, 스탑점
#     print('☆' * x)
#
# 2) 별 찍기 2
#
#
# print('☆' * 6)
# print('☆' * 5)
# print('☆' * 4)
# print('☆' * 3)
# print('☆' * 2)
# print('☆' * 1)
#
#
# for x in range(6, 0, -1): # 시작점, 스탑점, 움직이는점
#     print('☆' * x)
#
# 별 찍기 3
#
#
# for x in range(7, 0, 1):
#     print("" * x, '☆' * x)
#
# 실습 2) 구구단을 만들어 보자
#
#
# dan = int(input("단수는?"))
#
# for x in range(1, 10):
#     print("%d * %d = %d" % (dan, x, dan * x))
#
# for x in range(1, 100):
#     for y in range(1, 100):
#         print("%d * %d = %d" % (x, y, x * y))
#
# 실습 3) 숫자를 입력 받아 그 범위 안의 수 중 0~3의 배수를 출력
#
# 방법1)
# n = int(input("숫자를 입력하세요."))
# print(n)
#
# for x in range(0, n+1, 3):
#     print(x, end="\t") # end <-- 특정 문자를 넣어줄 수 있는 명령어.
# print()
#
# 방법2)
# for x in range(0, n+1, 3):
#     if x % 3 == 0:
#         print(x, end="\t")
#
#
# 실습 4) 숫자 두 개와 기호를 입력 받아 계산기를 만들어보자.
# 단, 사용자가 q를 입력하면 계산기 프로그램 종료
#
# while True:
#     n = input("계산기").split()  # 숫자 입력 값.
#     a = int(n[0])
#     b = int(n[2])
#     c = (n[1])
#     if c == "+":
#         print("%d + %d = %d" % (a, b, a + b))
#     elif c == "-":
#         print("%d - %d = %d" % (a, b, a - b))
#     elif c == "*":
#         print("%d * %d = %d" % (a, b, a * b))
#     elif c == "/":
#         print("%f / %f = %.2f" % (a, b, a / b))
#     elif c == "q":
#         print("기호 오류")
#         break
#
# 방법2)
# while True:
#     a = int(input("첫번째 수를 입력하세요"))
#     b = int(input("두번째 수를 입력하세요"))
#     sign = input("기호는?")
#     if sign == "+":
#         print(a + b)
#     elif sign == "-":
#         print(a - b)
#     elif sign == "*":
#         print(a * b)
#     elif sign == "/":
#         print(a / b)
#     else:
#         print("잘못된 기호")
#
#     if input("종료(y)?") == "y": break
#
# 방법3)
#
# while True:
#     a = int(input("첫번째 수를 입력하세요."))
#     if a == "q":
#         break
#     a = int(a)
#     b = int(input("두번째 수를 입력하세요."))
#     while True:    # 원하는 기호가 계속 입력될 때 까지 반복.
#         sign = input("기호:")
#         if sign in ["+", "-", "*", "/"]:
#             break
#     if sign == "+":
#         print(a + b)
#     elif sign == "-":
#         print(a - b)
#     elif sign == "*":
#         print(a * b)
#     elif sign == "/":
#         print(a / b)
#     else:
#         print("잘못된 기호")
#
# 실습5)  반학생들의 점수가 딕셔너리로 저장되어 있
# 을 때 값이 90점 이상인 학생들의 key 만 출
# 력하시오
#
# 예시) dicA = {1:94, 2:87, 3:91, 4:75, 5:92}
# 출력) 90점 이상 학생
# 1번
# 3번
# 5번
#
# dic = {1: 94, 2: 87, 3: 91, 4: 75, 5: 92}
# print(dic.keys())    # 키만 가져옴.
# print(dic.values())  # 값만 가져옴.
# print(dic.items())   # 키,값 가져옴.
#
# for no, score in dic.items():
#     # print(no, score)
#     if score >= 90:
#         print(no, "번", score, "점")
#
# 실습 6)
#
# listA = [‘홍길동’,’이순신’,’김순희’,’이철수’] 일 판매
# 수량을 입력 받아 히스토그램을 그리는 프로그램
# 을 만들어 봅시다
# 출력 예)
# 홍길동 : **********
# 이순신 : ***************
# 김순희 : ********
# 이철수 : ******
#
# 1. 사원의 판매수량 입력
# 2. 히스토그램 그리기
#
# lt = ["홍길동", "이순신", "김순희", "이철수"]
# li = {} # 판매수량 저장 할 딕셔너리
# # ls = [10, 15, 100, 20]
# # li = {"홍길동": 10, "이순신": 15, "김순희": 100, "이철수": 20}
#
# for name in lt:
#     li[name] = int(input(name + ":"))
#     # print(li)
#     for name, ne in li.items():
#         print(name + ":", '☆' * ne)

