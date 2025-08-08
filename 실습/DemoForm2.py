# DemoForm2.py
# DemoForm2.ui(화면) + DemoForm2.py(로직)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from bs4 import BeautifulSoup
import urllib.request
import re

#디자인 파일을 로딩
form_class = uic.loadUiType("C:\work\실습\DemoForm2.ui")[0]
# DemoForm 클래스 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # 첫번째 버튼 클릭 이벤트
    def firstClick(self):
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
        self.label.setText("오늘의 유머 크롤링 완료")

    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭")

#진입점을 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = DemoForm()
    myWindow.show()
    app.exit(app.exec_())