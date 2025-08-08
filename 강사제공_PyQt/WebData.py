# encoding:utf-8
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
import urllib.request
from bs4 import BeautifulSoup

class Form(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("WebData.ui", self)
        self.ui.show()

    @pyqtSlot()
    def slot_1st(self):
        data = urllib.request.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri')
        soup = BeautifulSoup(data, 'html5lib')
        cartoons = soup.findAll("td", attrs={"class":"title"})
        
        f = open("webtoon.txt", "a+", encoding="utf-8")

        for item in cartoons:
            title = item.find('a').text
            print(title)
            f.write(title+"\n")

        f.close()
        self.ui.label.setText("작업 완료!")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())



