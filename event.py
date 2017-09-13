# -*- coding: utf-8 -*-
"""重写keyPressEvent()事件处理函数"""
__author__ = 'Huang Lun'
import sys
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton


class Communicate(QObject):
    closeApp = pyqtSignal()  # 信号使用了pyqtSignal()方法创建，并且成为外部类Communicate类的属性


class Example1(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('事件处理')
        self.show()

    def keyPressEvent(self, e):
        # 如果我们点击了Esc按钮，应用将会被终止
        if e.key() == Qt.Key_Escape:
            self.close()


class Example2(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn1 = QPushButton("按钮1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("按钮2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('事件发送者')
        self.show()

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + '被点击了。')


class Example3(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)  # 把自定义的closeApp信号连接到QMainWindow的close()槽上

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('发射信号')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()  # 当我们在窗口上点击一下鼠标，closeApp信号会被发射。应用中断


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example3()
    sys.exit(app.exec_())
