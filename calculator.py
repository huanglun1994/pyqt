# -*- coding: utf-8 -*-
"""在我们的例子中，我们创建了一个全是按钮的网格布局"""
__author__ = 'Huang Lun'
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 实例化QGridLayout类，并且把这个类设为应用窗口的布局
        grid = QGridLayout()
        self.setLayout(grid)

        names = [
            'Cls', 'Bck', '', 'Close',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]  # 这些标签会在之后的按钮中使用

        positions = [(i, j) for i in range(5) for j in range(4)]  # 我们创建了一个网格的定位列表

        # 创建出按钮组件，并使用addWidget()方法向布局中添加按钮
        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
