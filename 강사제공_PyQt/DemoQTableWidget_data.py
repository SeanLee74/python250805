# DemoQTableWidget_Data.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#딕셔너리에 데이터를 저장하기(5행 3열 데이터) 
deviceDict = {
    'date': ['05-01', '05-02', '05-03', '05-04', '05-05'],
    'device': ['아이폰', '아이패드', '안드로이드폰', '윈도우폰', '윈도우타블렛'],
    'price': ['820000', '450000', '550000', '380000', '280000']
}
#컬럼의 이름을 딕셔너리에 미리 저장
column_idx_lookup = {'date': 0, 'device': 1, 'price': 2}

class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        #QTableWidget의 인스턴스를 생성하고 
        #크기를 변경하고 setRowCount()로 행의 갯수를 지정
        #setColumnCount()로 열의 갯수를 지정
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290, 290)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        #setEditTriggers()메서드를 사용해서 사용자가
        #QTableWidget의 아이템 항목을 수정할 수 없도록 셋팅한다. 
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #데이터를 채우는 코드를 메서드로 정의 
        self.setTableWidgetData()

    def setTableWidgetData(self):
        #상단에 출력할 컬럼이름
        column_headers = ['날짜', '디바이스', '가격']
        #0행에 컬럼명을 출력한다. 
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        for k, v in deviceDict.items():
            col = column_idx_lookup[k]
            for row, val in enumerate(v):
                #QTableWidget에 아이템으로 입력하려면 먼저
                #데이터를 QTableWidgetItem객체로 만들어야 함
                item = QTableWidgetItem(val)
                if col == 2:
                    #가격에 해당하는 열은 오른쪽 정렬을 하도록 셋팅
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                #해당 행과 열에 아이템을 추가한다. 
                self.tableWidget.setItem(row, col, item)

        #마지막으로 QTableWidget의 행과 열 크기를 각 위치에 저장된
        #아이템 길이에 맞추어 조정한다. 
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoWindow()
    demoWindow.show()
    app.exec_()