# demoFile.py

# 블럭을 선택하고 주석처리: ctrl + /
# 블럭을 선택하고 주석해제: ctrl + shift + /

# #파일쓰기
# f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
# f.write("첫번째\n두번째\n세번째\n")
# f.close()

# #파일읽기
# f = open("c:\\work\\test.txt", "rt", encoding="utf-8")
# print(f.read())
# f.close()

# #파일읽기 (한줄씩)
# f = open("c:\\work\\test.txt", "rt", encoding="utf-8")
# while True:
#     line = f.readline()
#     if not line: break
#     print(line.strip())
# f.close()

# #파일읽기 (raw string notation)
# f = open(r"c:\work\test.txt", "rt", encoding="utf-8")
# print(f.read())
# f.close()

#문자열 처리
strA = "파이썬은 강력해"
strB = "python is very powerful"
print(strA)
print(strB)
print(strB.capitalize())  # 첫 글자만 대문자로
print(strB.upper())       # 모두 대문자로
print("MBC2580".isalnum())  # 문자열이 알파벳과 숫자로만 구성되어 있는지 확인
print("2580".isdecimal())  # 문자열이 숫자로만 구성되어 있는지 확인
data = "    spam and ham   "
result = data.strip()  # 양쪽 공백 제거
print(data)
print(result)

data = "<<< spam and ham >>>"
result = data.strip("<> ")
print
print(result)

result2 = result.replace("spam", "spam egg")  # 문자열 치환
lst = result2.split()  # 문자열 분리
print(lst)

print(":)".join(lst))  # 리스트를 문자열로 합치기


#정규표현식
import re

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())  # 검색된 문자열 출력

# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())  # 검색된 문자열 출력

result = re.search("apple", "this is an apple")
print(result.group())  # 검색된 문자열 출력

result = re.search(r"\d{4}", "올해는 2025년입니다.")
print(result.group())  # 검색된 문자열 출력

result = re.search(r"\d{5}", "우리 동네는 51200입니다.")
print(result.group())  # 검색된 문자열 출력

text = "문의: test123@gmail.com 또는 admin@company.co.kr 으로 연락주세요."
result = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
if result:
    print(result.group())  # 검색된 이메일 주소 출력


