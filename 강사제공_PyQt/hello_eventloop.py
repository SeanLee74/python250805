# hello_eventloop.py
import sys
from PyQt5.QtWidgets import * 

app = QApplication(sys.argv)
label = QLabel("매우 간단한 앱, PyQt")
label.show()

print("event loop를 실행하기 전")
app.exec_()
print("event loop를 실행한 후")
