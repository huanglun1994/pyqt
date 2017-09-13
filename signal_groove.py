# -*- coding: utf-8 -*-
"""
在我们的例子中，我们显示了一个QtGui.QLCDNumber和一个QtGui.QSlider类。
我们拖动滑块条的把手，lcd数字会变化。
"""
__author__ = 'Huang Lun'
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)  # 将滑块条的valueChanged信号和lcd数字显示的display槽连接在一起。

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('信号槽')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
