# form2.py(로직 코딩) + form2.ui(화면을 XML문서 저장)
import sys 
#Qt패키지를 임포트 
from PyQt5.QtWidgets import *
from PyQt5 import uic 
#웹사이트에 페이지 실행을 요청
import urllib.request
from bs4 import BeautifulSoup

#디자인 문서를 로딩
form_class = uic.loadUiType("c:\\work\\form2.ui")[0]
#윈도우 클래스 정의(좀 더 기능이 많은 창 QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
        data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
        soup = BeautifulSoup(data, "html.parser")
        cartoons = soup.find_all("td", class_="title")
        f = open("c:\\work\\webtoon.txt", "a+", encoding="utf-8")
        for item in cartoons:
            title = item.find("a").text 
            print(title)
            f.write(title + "\n")
        f.close() 
        self.label.setText("웹 크롤링 작업 종료")
    def secondClick(self):
        self.label.setText("두번째 화면")
    def thirdClick(self):
        self.label.setText("세번째 화면~~")

#모듈을 직접 실행했는지를 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()