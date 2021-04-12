# 딕셔너리 : 순서가 없다.
#
# data = {"a": 10, "b": 20, "c": 30, "d": 40}
#
# print(data["b"])

#
# date = {"홍길동" : 20, "이순신" : 45}
# print(date["홍길동"], "살")

# date = {"홍길동": [20, 165.5], "이순신": 45}
#
# print(date["홍길동"][0])

# date = {"홍길동": {"나이": 20, "키": 165.5}, "이순신": {"나이": 45, "키": 188}}
#
# print(date["홍길동"]["키"])
#
# date= {1: ["홍길동", 20, 165.5], 2: ["이순신", 45, 188]}
# print(date[2][0])
#
# # 디셕너리에 데이터 추가
# data={}
# data["홍길동"] = 20
# data["이순신"] = [45, 170, 8]
# print(date)

# 실습) 컴퓨터 언어를 입력 받아 딕셔너리에 저장
# {"backend: java", "frontend": "html5"}

# lang = {}
#
# a = input("backend 언어는?")
# b = input("frontend 언어는?")
#
# lang["backend"] = a
# lang["frontend"] = b
# print(lang)

# 실습) 영화 순위 딕셔너리
# data = {1: "고질라", 2: "귀멸의 칼날", 3: "더박스"}
# print(list(data.keys()))
# print(list(data.values())[0])

# set:중복 데이터 허용불가

# asia = {"한국", "중국", "일본"}
# asia.add("베트남")
# asia.add("중국")
# asia.remove("일본")
# asia.update({"한국", "홍콩", "태국"})
# print(asia)
