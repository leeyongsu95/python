# 모듈
#
# import time
#
# print(time.localtime().tm_year, "년", end=" ", sep="")
# print(time.localtime().tm_mon, "월", end=" ", sep="")
# print(time.localtime().tm_mday, "일", end=" ", sep="")
# print(time.localtime().tm_hour, "시", end=" ", sep="")
# print(time.localtime().tm_min, "분", end=" ", sep="")
#
# import datetime
#
# now = datetime.datetime.now()
# print(now)
# print(now.strftime("%Y-%m-%d-%H:%M:%S"))
#
# 방법 선호!
# from datetime import datetime as a
# now = a.now()
# print(now)
# print(now.strftime("%Y-%m-%d-%H:%M:%S"))
#
# sleep 함수: 프로그램 실행 속도를 제어
#
# import time
# print("타이머 시작")
# time.sleep(3)
# print("타이머 3초 지남")
#
# 타이머 만들기.
# 1초 마다 화면에 타이머를 출력
# 결과
# 1 타이머 시작 1초 2초 3초 타이머 종료.
#
#
# 내가 한 방식)
# from time import sleep as a
#
# ti = int(input("초를 입력해주세요."))
# print("타이머 시작")
#
# for x in range(ti):
#     a(1)
#     print(x, "초 지남")
# print("타이머 종료")
#
#
#
# # 같이 한 방식)
# from time import sleep
#
# sec = int(input("몇초?"))
# print("타이머 시작")
# for x in range(sec):
#     sleep(1)
#     print(x, "초")
# print("종료")
#
#
# 난수 모듈
# 주사위 게임
# import random
# awin=0 #a이긴 횟수
# bwin=0 #b이긴 횟수
# while True:
#     a = random.randint(1,6)
#     b = random.randint(1,6)
#     print('A:', a, 'B:', b)
#     if a>b:
#         print('A승')
#     elif b>a:
#         print('B승')
#     else:
#         print('무승부')
#
#
#
#
# import random
#
# sample()
# print(random.sample(range(1, 46), 6))
# lotto = random.sample(range(1, 46), 6)
# print(lotto)
#
# choice()
# print(random.choice(["가위", "바위", "보"]))
#
#
# shuffle(): 섞는다
# data = ["나비", "나비", "별", "별", "꽃", "꽃"]
# random.shuffle(data)
# print(data)
#
# import turtle # 그래픽 모듈
#
# turtle.shape("turtle")
# turtle.color("red")
#
# for x in range(4):
#     turtle.forward(220)
#     turtle.right(160)
#
# turtle.done()