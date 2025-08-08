# DemoQVBoxLayout.py
import sys
from PyQt5.QtWidgets import *

class DemoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        self.textEdit = QTextEdit()
        self.pushButton= QPushButton('저장')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.pushButton)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoWindow()
    demoWindow.show()
    app.exec_()