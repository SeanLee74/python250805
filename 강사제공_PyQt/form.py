# form.py(로직 코딩) + form.ui(화면을 XML문서 저장)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#디자인 문서를 로딩
form_class = uic.loadUiType("c:\\work\\form.ui")[0]
#윈도우 클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")
#모듈을 직접 실행했는지를 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()