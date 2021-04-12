# 반복문: for

# data = [1, 2, 3, 4, 5]

# for x in [1, 2, 3, 4, 5]:
#     print("python", x)

# data = ["이씨", "김씨", "서씨", "임씨"]

# for x in data:
#     print(x)
#
# for x in [0, 1, 2]:
#     print(data[x])

#실습)0~9까지 출력

# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for x in data:
#     print(x)

# 정수를 생성
# range 함수란 (start 시작 값, stop 멈추는 값, step 움직이는 값 )

# print(list(range(10, 50, 3)))
# print(list(range(10)))  #stop
# print(list(range(10, 20))) #start, stop

# for x in range(0, 10, 2):
#     print(x)

# 합계를 구하기

# 1~ 10 까지 출력
# s = 0 # 합계를 저장할 변수
#
# for x in range(1, 10):
#     s += x  # s = s + x
# print(s)

# 실습) 사용자에게 입력을 받아 1부터 그 합계를 출력

# ur = int(input("수를 입력해 주세요"))
# print(ur)
#
# s = 0
#
# for x in range(1, ur+1):
#     s += x
# print(s)

# 실습) 1부터 100까지 합이 2000이 넘을때의 수를 출력.

# s = 0
#
# for x in range(1, 101):
#     s += x
#     if s > 2000:
#         break # 반복문을 종료할때
# print("x = ", x, "s = ", s)

# 실습) 멍청이라는 글자가 발견되면 강퇴.

# data = ["안녕", "반가워", "고마워", "오늘 만나"]
# bl = ["바보", "멍청이"]
#
# for x in data:
#     print(x)
#     if x in bl:
#         print("강퇴 되었습니다.")
#         break
# else:   # for 문이 정상 수행했다면 (break 실행 하지 않음.)
#     print("바른말 유저")

# continue: 계속 진행
# data = [3, 4, 6, 8, 10]
#
# for x in data:
#     if x %2 == 1: continue
#     print(x, "짝수")

# 실습) 어떤 학생의 점수 리스트가 주어졌을 때 모든 점수가
# 60점이 넘으면 합격하는 프로그램을 작성하시오.
# 예) 점수 리스트: [65, 45, 95, 55, 70]
# 또는 [90, 45, 42, 55, 48]

# data = input("점수를 입력해주세요.").split(",")
# print(data)
# data = map(int, data) # map 함수 int형으로 변경
# print(list(data))

# 방법2)

# data = input("점수를 입력해주세요.").split(",")
# print(data)

# for x in data:
#     print(x)
#     if x < 60:
#         print("탈락")
#         break
# else:
#     print("합격")

# 실습) 어떤 학생의 점수 리스트가 주어졌을 때 모든 점수가
# 300점이 넘으면 합격하는 프로그램을 작성하시오.
# 예) 점수 리스트: [65, 45, 95, 55, 70]
# 또는 [90, 45, 42, 55, 48]

# s = 0
# data = [65, 65, 50, 55, 70]

#(
# data = input("점수를 입력해주세요.").split(",")
# data = map(int, data)
# )

# for x in data:
#     s += x
#     if s > 300:
#         print("합격")
#         break
# else:
#     print("불합격")
