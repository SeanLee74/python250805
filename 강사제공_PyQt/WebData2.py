import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
import urllib.request
from bs4 import BeautifulSoup

class Form(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        #창의 시작위치와 폭, 높이(x,y,width,height) 
        self.setGeometry(50, 50, 400, 400)
        
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.resize(400, 400)
        self.tableWidget.setRowCount(10)  #행의 갯수 
        self.tableWidget.setColumnCount(1)  #컬럼의 갯수 
        self.setTableWidgetData()

    def setTableWidgetData(self):
        data = urllib.request.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri')
        soup = BeautifulSoup(data, 'html.parser')
        cartoons = soup.find_all("td", attrs={"class":"title"})
        
        f = open("webtoon.txt", "a+", encoding="utf-8")

        row = 0 
        for item in cartoons:
            title = item.find('a').text
            print(title)
            f.write(title+"\n")
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
            row += 1
            
        f.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywindow = Form()
    mywindow.show()
    app.exec_()



