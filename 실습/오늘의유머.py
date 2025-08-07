# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f = open('todayhumor.txt', 'wt', encoding='utf-8')

for n in range(1,11):
        #오늘이 유머 베스트 게시판
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.findAll('td', attrs={'class':'subject'})

#<td class="subject">
# <a href="" target="_top">여자 연예인들의 이상형이라는 남자 연예인</a>
# <span class="list_memo_count_span"> [25]</span>
# <span style="margin-left:4px;">
# <img src="" style="vertical-align:middle; margin-bottom:1px;"> </span>
# </td>

        for item in list:
                try:
                        #내부에 <a> 태그가 있는 경우
                        title = item.find('a').text.strip()  # 문자열 앞뒤 공백 제거                                                 
                        if (re.search('한국', title)):
                                print(title)                                
                                f.write(title + '\n')                        
                        
                except:
                        pass
        
f.close()