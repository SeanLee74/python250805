import re

# 이메일 주소 목록 (10개 준비)
emails = [
    "test123@gmail.com",         # 올바른 이메일
    "admin@company.co.kr",       # 올바른 이메일
    "user.name@domain.com",      # 올바른 이메일
    "user_name@domain.co",       # 올바른 이메일
    "user-name@domain.org",      # 올바른 이메일
    "user+mailbox@domain.info",  # 올바른 이메일
    "user@sub.domain.com",       # 올바른 이메일
    "invalid-email@domain",      # 잘못된 이메일 (마침표 뒤 글자가 너무 짧음)
    "noatsign.com",              # 잘못된 이메일 (@가 없음)
    "user@domain.c"              # 잘못된 이메일 (마침표 뒤 글자가 너무 짧음)
]

# 정규표현식 패턴 설명
# ^ : 이메일의 시작을 의미해요
# [a-zA-Z0-9._%+-]+ : 이름 부분에는 영어, 숫자, 점, 밑줄, 퍼센트, 더하기, 빼기가 올 수 있어요 (한 글자 이상)
# @ : 꼭 @가 있어야 해요
# [a-zA-Z0-9.-]+ : @ 뒤에는 영어, 숫자, 점, 빼기가 올 수 있어요 (한 글자 이상)
# \. : 점(.)이 꼭 있어야 해요
# [a-zA-Z]{2,} : 점 뒤에는 영어가 2글자 이상 있어야 해요 (예: com, net, kr)
# $ : 이메일의 끝을 의미해요

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

for email in emails:
    # 이메일이 패턴과 맞는지 확인해요
    if re.match(pattern, email):
        print(f"유효한 이메일: {email}")  # 맞으면 '유효한 이메일'이라고 출력해요
    else:
        print(f"유효하지 않은 이메일: {email}")  # 틀리면 '유효하지 않은 이메일'이라고