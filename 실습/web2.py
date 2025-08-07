#web2.py
from bs4 import BeautifulSoup
import urllib.request
import re

#파일로 저장
f = open('clien.txt', 'w', encoding='utf-8')

#페이징 처리(번호를 생성)
for i in range(0, 10):
    url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" + str(i)
    print(url)
    # 함수 체인(메소드 체인)
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, 'html.parser')
    for tag in soup.find_all('span', attrs={'data-role': 'list-title-text'}):
        # 모든 연속된 공백 문자(스페이스, 탭, 줄바꿈 등)를 하나의 공백으로 치환
        title = tag.text.strip()
        if re.search('아이폰',title):
            print(title)
            f.write(title + '\n')

# 파일 닫기
f.close()

# <span class="subject_fixed" data-role="list-title-text" title="아이폰 13미니 256 팝니다">
#     아이폰 13미니 256 팝니다
# </span>