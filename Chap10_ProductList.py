import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

#DB파일이 없으면 만들고 있다면 접속한다. 
if os.path.exists("ProductList.db"):
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
else: 
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
    cur.execute(
        "create table Products (id integer primary key autoincrement, Name text, Price integer);")

#디자인 파일을 로딩
form_class = uic.loadUiType("Chap10_ProductList.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_database()
        
        # 초기값 셋팅 
        self.id = 0 
        self.name = ""
        self.price = 0 

        # UI 초기화
        self.init_ui()

    def init_database(self):
        """데이터베이스 초기화 및 연결"""
        db_path = "ProductList.db"
        is_new_db = not os.path.exists(db_path)
        
        try:
            self.con = sqlite3.connect(db_path)
            self.cur = self.con.cursor()
            
            if is_new_db:
                self.cur.execute(
                    "CREATE TABLE Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);")
                self.con.commit()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"데이터베이스 연결 오류: {str(e)}")
            sys.exit(1)

    def init_ui(self):
        """UI 초기화"""
        # QTableWidget 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID","제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)

        # 시그널 연결
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        self.tableWidget.doubleClicked.connect(self.doubleClick)

    def addProduct(self):
        """제품 추가"""
        try:
            name = self.prodName.text().strip()
            price = self.prodPrice.text().strip()
            
            if not name or not price:
                QMessageBox.warning(self, "입력 오류", "제품명과 가격을 입력하세요.")
                return

            self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", 
                (name, int(price)))
            self.con.commit()
            self.getProduct()
            self.clearInputs()
        except ValueError:
            QMessageBox.warning(self, "입력 오류", "가격은 숫자로 입력하세요.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"데이터 추가 오류: {str(e)}")

    def updateProduct(self):
        """제품 수정"""
        try:
            prod_id = self.prodID.text().strip()
            name = self.prodName.text().strip()
            price = self.prodPrice.text().strip()
            
            if not all([prod_id, name, price]):
                QMessageBox.warning(self, "입력 오류", "모든 필드를 입력하세요.")
                return

            self.cur.execute("UPDATE Products SET Name=?, Price=? WHERE id=?;", 
                (name, int(price), int(prod_id)))
            self.con.commit()
            self.getProduct()
            self.clearInputs()
        except ValueError:
            QMessageBox.warning(self, "입력 오류", "ID와 가격은 숫자로 입력하세요.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"데이터 수정 오류: {str(e)}")

    def removeProduct(self):
        """제품 삭제"""
        try:
            prod_id = self.prodID.text().strip()
            
            if not prod_id:
                QMessageBox.warning(self, "입력 오류", "삭제할 제품의 ID를 입력하세요.")
                return

            reply = QMessageBox.question(self, '삭제 확인', 
                '정말로 이 제품을 삭제하시겠습니까?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.cur.execute("DELETE FROM Products WHERE id=?;", (int(prod_id),))
                self.con.commit()
                self.getProduct()
                self.clearInputs()
        except ValueError:
            QMessageBox.warning(self, "입력 오류", "ID는 숫자로 입력하세요.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"데이터 삭제 오류: {str(e)}")

    def getProduct(self):
        """제품 목록 조회"""
        try:
            self.tableWidget.clearContents()
            self.cur.execute("SELECT * FROM Products;")
            
            for row, item in enumerate(self.cur):
                self.tableWidget.setItem(row, 0, self.createTableItem(str(item[0]), True))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(item[1])))
                self.tableWidget.setItem(row, 2, self.createTableItem(str(item[2]), True))
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"데이터 조회 오류: {str(e)}")

    def createTableItem(self, text, align_right=False):
        """테이블 아이템 생성 헬퍼 메서드"""
        item = QTableWidgetItem(text)
        if align_right:
            item.setTextAlignment(Qt.AlignRight)
        return item

    def clearInputs(self):
        """입력 필드 초기화"""
        self.prodID.clear()
        self.prodName.clear()
        self.prodPrice.clear()

    def doubleClick(self):
        """테이블 더블클릭 처리"""
        row = self.tableWidget.currentRow()
        self.prodID.setText(self.tableWidget.item(row, 0).text().strip())
        self.prodName.setText(self.tableWidget.item(row, 1).text().strip())
        self.prodPrice.setText(self.tableWidget.item(row, 2).text().strip())

    def closeEvent(self, event):
        """프로그램 종료 시 리소스 정리"""
        try:
            if hasattr(self, 'cur'):
                self.cur.close()
            if hasattr(self, 'con'):
                self.con.close()
        except sqlite3.Error:
            pass
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()




