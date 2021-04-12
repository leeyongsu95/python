# ctrl+/ : 주석 설정/해제
# 변수: 데이터를 저장하기 위한 공간
# 변수명: 저장된 데이터를 접근하기 위한 이름
# = : 대입연산자
#사칙연산: +,-, *, /,%,//

#실습)시분초 구하기
# s = 10000
# t = s//3600
# print(t, "시간")
#
# r = s % 3600
# m=r//60
# print(m, "분")
#
# s = r%60
# print(s, "초")

# 포맷 문자열을 이용한 사칙연산
# %.자리수<- f (%.2f) 자리수 내림

a = 30; b = 20

print(a, "+", b, "=", a + b)
print("%d - %d = %d" %(a, b, a-b))
print("%d * %d = %d" %(a, b, a*b))
print("%d / %d = %.2f" %(a, b, a/b))
print("%d %% %d = %.2f" %(a, b, a%b))

# a = 50
# b = 3
# print("a + b =", a + b)
# print("a - b =", a - b)
# print("a * b =", a * b)
# print("a / b =", round(a/b, 3))
# print("a / b = %.2f" %(a/b))
# print("a % b = ", a%b)  #나머지
# print("a // b =",a//b)  #몫