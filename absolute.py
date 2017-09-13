# -*- coding: utf-8 -*-
"""
我们使用move()方法来定位我们的组件。
例子中我们使用move()方法定位了一些标签组件。
在使用move()方法时，我们给move()方法提供了x和y坐标作为参数。
move()使用的坐标系统是从左上角开始计算的。x值从左到右增长。y值从上到下增长。
"""
__author__ = 'Huang Lun'
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
