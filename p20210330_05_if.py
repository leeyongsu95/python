# 조건문
#
# a = 1
# # if 조건문:
# if a > 0:
#     print("양수", a)
# else:
#     print("음수", a)
#
#
# 실습1) 회원등급 출력
# a가 90보다 크면 good 아니면 try
#
# a = int(input("점수는?"))
#
# if a > 90:
#     print("good")
# else:
#     print("try")
#
# 실습2) 비밀번호 체크
# 비밀번호가 일치하면 "문이 열립니다."
# 비밀번호가 일치하지 않으면 "다시 확인하세요."
#
# 내 코딩 방식
# pw = input("비밀번호를 입력하세요.") # 입력 비밀번호
#
# if pw == "1234":
#     print("문이 열립니다")
# else:
#     print("비밀번호를 다시 확인하세요.")
#
# pw = "1234" # 기본 등록된 비밀번호
# ipw = input("비밀번호를 입력하세요.") # 기본 등록된 비밀번호
#
# if pw == ipw:
#     print("문이 열립니다")
# else:
#     print("비밀번호를 다시 확인하세요.")
#
# 실습) 어떤수가 짝수면 "짝수" 홀수면 "홀수" 출력
#
# a = int(input("숫자를 입력하세요."))
#
# if a == 0:
#     print("짝수도 홀수도 아닙니다.")
# elif a % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")
#
#
# 실습) 90~점 A, 80~89점 B, 79~70 C, 60~69 D, 59~F
#
# sc = int(input("점수를 입력해주세요"))
#
# if sc >= 90:
#     print("A 학점입니다.")
# elif sc >= 80:
#     print("B 학점입니다.")
# elif sc >= 70:
#     print("C 학점입니다.")
# elif sc >= 60:
#     print("D 학점입니다.")
# else:
#     print("F 학점입니다.")
#
# 실습) 이름/신장/몸무게를 입력 받고 적정 체중 여부를 출력하세요.
#
# weinght = int(input("몸무게를 입력하세요."))
# height = int(input("키를 입력하세요."))
# normal = (height - 100)*0.9
# print("정상 체중", normal, "kg입니다")
#
# if weinght < normal * 0.95:
#     print("미달")
# elif weinght <= normal * 1.05:
#     print("정상")
# else:
#     print("과체중")
#
# 실습) 계산기를 만들어 보세요
# 30 + 20 = 50
#
# ps = int(input("숫자를 입력해주세요(+, -, *, /)"))
# fs = int(input("숫자를 입력해주세요(+, -, *, /)"))
#
# sign0 = '+'
# sign1 = '-'
# sign2 = '*'
# sign3 = '/'
#
# if sign0 == '+':
#      print(ps+fs)
# elif sign1 == '-':
#     print(ps + fs)
# elif sign2 == '*':
#     print(ps + fs)
# else:
#     print(ps + fs)
#
# 실습2)

# data = input("계산식은?").split()
#
# a = int(data[0])
# b = int(data[2])
# sign = data[1]
#
# if sign == "+":
#     print("%d + %d = %d" % (a, b, a+b))
# elif sign == "-":
#     print("%d - %d = %d" % (a, b, a-b))
# elif sign == "*":
#     print("%d * %d = %d" % (a, b, a*b))
# elif sign == "/":
#     print("%f / %f = %.2f" % (a, b, a/b))
# else:
#     print("계산식을 입력해주세요.")

# 실습 3)
#
# import os
# print(os.listdir())
#
# data = input("계산식은?")
# cal = eval(data)  # eval 바로 계산 해주는 함수 // 실무에서는 사용 금지
#
# print(eval(data))
#
# 실습 4) 두 수를 입력 받아서 큰 수를 화면에 출력
#
# 방법1)
# ly = int(input("수를 입력해주세요."))
# ys = int(input("수를 입력해주세요."))
#
# if ly > ys:
#     print("ly의", ly)
# elif b > a:
#     print("ys 의 ", ys)
# else:
#     print("같다")
#
# 방법2)
# ly = input("수를 입력해주세요").split()
# a = int(ly[0])
# b = int(ly[1])
#
# if a > b:
#     print("a 의 ", a)
# elif b > a:
#     print("b 의 ", b)
# else:
#     print("같다")
#
# 실습)
# sh = int(input("물품 금액:"))
# py = int(input("낸 금액:"))
#
# if py > sh:
#     print("거스름돈:", py - sh)
# elif py < sh:
#     print("잔액 부족", sh - py)
# else:
#     print("결제 완료.")
#
# 논리연산자
#
# a = 10; b = 20
# print(a > 0 and b > 0)  # a가 0 보다 크고, b가 0보다 크면 true
# print(a > 0 and b < 0)  # a가 0 보다 크고, b가 0보다 작으면 false
# print(a > 0 or b < 0)  # or 둘중에 하나만 참이여도 true
# print(not (a > 0))
#
# a = int(input("첫번째 수를 입력해주세요"))
# b = int(input("두번째 수를 입력해주세요"))
#
# ) a = 10; b = 10
#
# if a == 0 and b > 0:
#     print("0이 아닌 수를 입력해주세요")
# elif a > 0 and b > 0:
#     print("= 양수")
# elif a > 0 or b > 0:
#     print("= 음수")
# else:
#     print("둘다 음수")
#
# price = ({"1": ["자장면", 5000], "2": ["짬뽕", 6000],
#           3: ["설렁탕", 8000], 4: ["비빔밥", 9000],
#           5: ["피자", 11000], 6: ["스파게티", 10000]}
#         )
# print("-" * 22) # - 생성 명령어
# print("[푸드] 금일 식사")
# print("-" * 22)
#
# fd = input("1.자장면\n2.짬뽕\n3.설렁탕\n4.비빔밥\n5.피자\n6.스파게티")
# print("-" * 15)
# no = input("메뉴 선택")
# print(price[no][0], "선택")
# print(price[no][1], "원")
#
# if no == "1" or no == "2":
#     print("중식으로 가세요.")
# elif no == "3" or no == "4":
#     print("한식으로 가세요.")
# elif no == "5" or no == "6":
#     print("양식으로 가세요.")
# else:
#     print("번호를 다시 입력해주세요.")
#
# 방식1) in= 포함여부
#
# if no in [1, 2]:
#     print("중식으로 가세요.")
# elif no in [3, 4]:
#     print("한식으로 가세요.")
# elif no in [5, 6]:
#     print("양식으로 가세요.")
# else:
#     print("번호를 다시 입력해주세요.")
#
# 방식2)
#
# print("-" * 22) # - 생성 명령어
# print("[푸드] 금일 식사")
# print("-" * 22)
#
# fd = input("1.자장면\n2.짬뽕\n3.설렁탕\n4.비빔밥\n5.피자\n6.스파게티")
# print("-" * 15)
# no = input("메뉴 선택")
#
#
# if no == "1" or no == "2":
#     print("중식으로 가세요.")
# elif no == "3" or no == "4":
#     print("한식으로 가세요.")
# elif no == "5" or no == "6":
#     print("양식으로 가세요.")
# else:
#     print("번호를 다시 입력해주세요.")
#
# price = ({"1": ["자장면", 5000, "중식"], "2": ["짬뽕", 6000, "중식"],
#           3: ["설렁탕", 8000, "한식"], 4: ["비빔밥", 9000, "한식"],
#           5: ["피자", 11000, "양식"], 6: ["스파게티", 10000, "양식"]}
#         )
# print("-" * 22) # - 생성 명령어
# print("[푸드] 금일 식사")
# print("-" * 22)
#
# fd = input("1.자장면\n2.짬뽕\n3.설렁탕\n4.비빔밥\n5.피자\n6.스파게티")
# print("-" * 15)
#
# no = input("메뉴 선택")
# myk = price.keys()
#
# print(myk)
#
# if no in myk:
#     print(price[no][0], "선택")
#     print(price[no][1], "원")
#     print(price[no][2], "코너")
# else:
#     print("다시 입력해주세요.")