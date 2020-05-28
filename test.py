#QInputDialog

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('输入对话框')
        layout = QFormLayout()

        self.button1 = QPushButton('获取列表中选项')
        self.linedit = QLineEdit()
        self.button1.clicked.connect(self.getItem)

        self.button2 = QPushButton('获取字符串')
        self.linedit2 = QLineEdit()
        self.button2.clicked.connect(self.getText)

        self.button3 = QPushButton('获取整数')
        self.linedit3 = QLineEdit()
        self.button3.clicked.connect(self.getInt)

        layout.addRow(self.button1,self.linedit)
        layout.addRow(self.button2,self.linedit2)
        layout.addRow(self.button3,self.linedit3)
        self.setLayout(layout)

    def getItem(self):
        items = ('C','C++','Ruby','Python','Java')
        item,ok = QInputDialog.getItem(self,'请选择编程语言','语言列表',items)
        if ok and item:
            self.linedit.setText(item)

    def getText(self):
        text,ok = QInputDialog.getText(self,'文本输入框','输入姓名')
        if ok and text:
            self.linedit2.setText(text)

    def getInt(self):
        num,ok = QInputDialog.getInt(self,'整数输入框','输入数字')
        if ok and num:
            self.linedit3.setText(num)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    app.exit(app.exec_())
