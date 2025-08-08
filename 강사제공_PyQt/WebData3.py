import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
import urllib.request
from bs4 import BeautifulSoup
import webbrowser   #브라우저로 넘기는 경우 
import re 

class Form(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        #창의 시작위치와 폭, 높이(x,y,width,height) 
        self.setGeometry(200, 200, 800, 800)
        
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.resize(800, 600)
        self.tableWidget.setRowCount(10)  #행의 갯수 
        self.tableWidget.setColumnCount(2)  #컬럼의 갯수 
        #컬럼의 폭을 지정한다. 0번 1번 
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 300)
        
        self.setTableWidgetData()
        self.tableWidget.doubleClicked.connect(self.doubleClicked)


    def setTableWidgetData(self):
        for n in range(0,10):
            #클리앙의 중고장터 주소 
            data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
            req = urllib.request.Request(data)
            data = urllib.request.urlopen(req).read()
            page = data.decode('utf-8', 'ignore')
            soup = BeautifulSoup(page, 'html.parser')
            list = soup.findAll('a', attrs={'class':'list-subject'})

            f = open("clien.txt", "a+", encoding="utf-8")

            for item in list:
                    try:
                            title = item.text
                            if (re.search('맥', title)):
                                    print(title.strip())
                                    print('https://www.clien.net'  + item['href'])
                                    row = 0 
                                    f.write(title+"\n")
                                    f.write(link + "\n")
                                    #행데이터로 출력 
                                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
                                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(link))
                                    row += 1
                    except:
                            pass

        


            
            f.close()

    def doubleClicked(self):
        url = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
        webbrowser.open("http://comic.naver.com/" + url) 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywindow = Form()
    mywindow.show()
    app.exec_()



