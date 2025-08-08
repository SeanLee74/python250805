import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor, QPalette, QFont

class ProductManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initDB()  # 데이터베이스 먼저 초기화
        self.initUI()  # 그 다음 UI 초기화

    def initDB(self):
        self.conn = sqlite3.connect('products.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS MyProducts 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT NOT NULL,
                             price INTEGER NOT NULL)''')
        self.conn.commit()

    def initUI(self):
        # 중앙 위젯 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 입력 폼 그룹
        form_group = QGroupBox('제품 정보')
        form_layout = QFormLayout()

        # 입력 필드
        self.name_edit = QLineEdit()
        self.price_edit = QLineEdit()
        self.search_edit = QLineEdit()

        form_layout.addRow('제품명:', self.name_edit)
        form_layout.addRow('가격:', self.price_edit)
        form_layout.addRow('검색:', self.search_edit)
        form_group.setLayout(form_layout)

        # 버튼 그룹
        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton('추가')
        self.update_btn = QPushButton('수정')
        self.delete_btn = QPushButton('삭제')
        self.search_btn = QPushButton('검색')

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.update_btn)
        btn_layout.addWidget(self.delete_btn)
        btn_layout.addWidget(self.search_btn)

        # 테이블 위젯
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['ID', '제품명', '가격'])

        # 버튼 이벤트 연결
        self.add_btn.clicked.connect(self.add_product)
        self.update_btn.clicked.connect(self.update_product)
        self.delete_btn.clicked.connect(self.delete_product)
        self.search_btn.clicked.connect(self.search_product)
        self.table.itemClicked.connect(self.select_product)

        # 레이아웃 배치
        layout.addWidget(form_group)
        layout.addLayout(btn_layout)
        layout.addWidget(self.table)

        # 스타일 시트 설정
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QGroupBox {
                background-color: white;
                border: 2px solid #3498db;
                border-radius: 5px;
                margin-top: 10px;
                font-weight: bold;
            }
            QGroupBox::title {
                color: #2980b9;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 3px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QLineEdit {
                padding: 5px;
                border: 2px solid #bdc3c7;
                border-radius: 3px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
            QTableWidget {
                background-color: white;
                gridline-color: #bdc3c7;
                border: none;
            }
            QTableWidget::item:selected {
                background-color: #e8f6ff;
                color: black;
            }
            QHeaderView::section {
                background-color: #3498db;
                color: white;
                padding: 5px;
                border: none;
            }
        """)

        # 폰트 설정
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        form_group.setFont(title_font)

        # 버튼 색상 커스터마이징
        self.add_btn.setStyleSheet("background-color: #27ae60;")
        self.update_btn.setStyleSheet("background-color: #f39c12;")
        self.delete_btn.setStyleSheet("background-color: #e74c3c;")
        self.search_btn.setStyleSheet("background-color: #9b59b6;")

        # 테이블 위젯 설정
        self.table.setAlternatingRowColors(True)
        self.table.setStyleSheet("""
            QTableWidget {
                alternate-background-color: #f9f9f9;
            }
        """)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # 윈도우 설정
        self.setWindowTitle('💻 전자제품 관리 시스템')
        self.setGeometry(300, 300, 800, 600)
        
        # 여백 설정
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)
        
        self.show()
        
        # 초기 데이터 로드
        self.load_data()

    def load_data(self):
        self.cursor.execute("SELECT * FROM MyProducts")
        data = self.cursor.fetchall()
        self.table.setRowCount(len(data))
        
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))

    def add_product(self):
        name = self.name_edit.text()
        price = self.price_edit.text()
        
        if name and price:
            try:
                price = int(price)
                self.cursor.execute("INSERT INTO MyProducts (name, price) VALUES (?, ?)", 
                                  (name, price))
                self.conn.commit()
                self.load_data()
                self.clear_inputs()
            except ValueError:
                QMessageBox.warning(self, '경고', '가격은 숫자로 입력해주세요.')
        else:
            QMessageBox.warning(self, '경고', '모든 필드를 입력해주세요.')

    def update_product(self):
        selected = self.table.selectedItems()
        if selected:
            row = selected[0].row()
            product_id = self.table.item(row, 0).text()
            name = self.name_edit.text()
            price = self.price_edit.text()
            
            if name and price:
                try:
                    price = int(price)
                    self.cursor.execute("UPDATE MyProducts SET name=?, price=? WHERE id=?",
                                      (name, price, product_id))
                    self.conn.commit()
                    self.load_data()
                    self.clear_inputs()
                except ValueError:
                    QMessageBox.warning(self, '경고', '가격은 숫자로 입력해주세요.')
            else:
                QMessageBox.warning(self, '경고', '모든 필드를 입력해주세요.')
        else:
            QMessageBox.warning(self, '경고', '수정할 항목을 선택해주세요.')

    def delete_product(self):
        selected = self.table.selectedItems()
        if selected:
            row = selected[0].row()
            product_id = self.table.item(row, 0).text()
            
            reply = QMessageBox.question(self, '삭제 확인', 
                                       '선택한 항목을 삭제하시겠습니까?',
                                       QMessageBox.Yes | QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                self.cursor.execute("DELETE FROM MyProducts WHERE id=?", (product_id,))
                self.conn.commit()
                self.load_data()
                self.clear_inputs()
        else:
            QMessageBox.warning(self, '경고', '삭제할 항목을 선택해주세요.')

    def search_product(self):
        search_text = self.search_edit.text()
        if search_text:
            self.cursor.execute("SELECT * FROM MyProducts WHERE name LIKE ?",
                              ('%' + search_text + '%',))
            data = self.cursor.fetchall()
            self.table.setRowCount(len(data))
            
            for i, row in enumerate(data):
                for j, val in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(str(val)))
        else:
            self.load_data()

    def select_product(self):
        selected = self.table.selectedItems()
        if selected:
            row = selected[0].row()
            self.name_edit.setText(self.table.item(row, 1).text())
            self.price_edit.setText(self.table.item(row, 2).text())

    def clear_inputs(self):
        self.name_edit.clear()
        self.price_edit.clear()

    def closeEvent(self, event):
        self.conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProductManager()
    sys.exit(app.exec_())