#문자열 다루기

txt = "python is easy!"

print(txt[0])
print(txt[-1])  # 마지막인덱스
print(txt[7:9]) # strt index : stop index
print(txt[:2])  # 0:2
print(txt[-5:]) # 5부터 끝까지

# 실습
# 1. s = "my house" 가 있을 때 house 를 화면에 출력하세요.
# 2. txt= "012345678901234567890123456" 일 때

s = "my house"
print(s[3:9])

txt = "012345678901234567890123456"
print(txt[:10])
print(txt[10:20])
print(txt[20:])
