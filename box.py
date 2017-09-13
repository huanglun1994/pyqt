# -*- coding: utf-8 -*-
"""
例子在右下角放置了两个按钮。当我们改变应用窗口大小时，它们会相对于应用窗口不改变位置。
在这个例子中我们使用了QHBoxLayout和QVBoxLayout两个布局类。
"""
__author__ = 'Huang Lun'
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 创建了两个按钮
        okButton = QPushButton('确定')
        cancelButton = QPushButton('取消')

        # 创建了一个水平箱布局，并且增加了一个拉伸因子和两个按钮。
        # 拉伸因子在两个按钮之前增加了一个可伸缩空间。这会将按钮推到窗口的右边。
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 为了创建必要的布局，我们把水平布局放置在垂直布局内。
        # 拉伸因子将把包含两个按钮的水平箱布局推到窗口的底边
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)  # 设置窗口的主布局

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
