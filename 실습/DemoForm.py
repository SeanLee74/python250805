# DemoForm.py
# DemoForm.ui(화면) + DemoForm.py(로직)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인 파일을 로딩
form_class = uic.loadUiType("C:\work\실습\DemoForm.ui")[0]
# DemoForm 클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 문자열 출력")

#진입점을 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = DemoForm()
    myWindow.show()
    app.exit(app.exec_())