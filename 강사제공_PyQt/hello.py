# hello.py
import sys
from PyQt5.QtWidgets import * 

app = QApplication(sys.argv)
label = QLabel("첫번째 PyQt")
label.show()
app.exec_()

