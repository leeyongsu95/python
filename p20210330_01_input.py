#사용자에게 입력받기

# a = input("비밀번호를 입력하세요")

# print("입력한 값은", a)

#실습) 나이를 입력받아 화면에 출력

# a = input("당신의 나이는?")

# print("당신의 나이는", a + "입니다")

# #실습) 날씨를 입력받아 오늘의 날씨 출력
# #예) 오늘의 날씨는 맑음

# b = input("오늘의 날씨는?")
# txt = "오늘의 날씨는"
# c = "입니다"

# print(txt, b+c)

#도움말 출력
#help(print)

#사용자가 입력한 값에 100을 더해서 출력
# a = input("숫자는?")
# # a = int(a) # int 정수를 변환해서 반환해주는 함수
# a = float(a) # float 실수를 변환해서 반환해주는 함수

# print(a + 100)

#실습) 사용자에게 두 수를 입력 받아 사칙연산 프로그램

# a = float(input("국어 점수:"))
# b = float(input("수학 점수:"))
#
# print("%d + %d = %d" %(a, b, a + b))
# print("%f - %f = %.2f" %(a, b, a - b))
# print("%f * %f = %.2f" %(a, b, a * b))
# print("%f / %f = %.2f" %(a, b, a / b))
# print("두 수를 더한 값은", a+b, "점입니다")

#2)
# 방법1)

# date = input("두 수는?")
# a = int(date.split()[0])
# b = int(date.split()[1])
#
# print(a, "+", b, "=", a + b)

# 방법2)
# date = input("두 수는?").split()

# a, b = map(int, date) # date의 각 값을 int 함수를 적용한 후 a,b에 대입
# print(a, "+",  b, "=",  a + b)

# # 실습 반지름을 사용자로 부터 입력 받아 원의 넓이를 구해보세요. (원주율 3.14)

# a = float(input("반지름의 길이는:"))

# print("원의 넓이는", a**2 * 3.14, "입니다")
