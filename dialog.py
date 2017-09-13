# -*- coding: utf-8 -*-
"""
例子中有一个按钮和一个单行编辑框组件。按下按钮会显示输入对话框用于获得一个字符串值。
在对话框中输入的值会在单行编辑框组件中显示
"""
__author__ = 'Huang Lun'
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication, QFrame, QColorDialog,
                             QVBoxLayout, QSizePolicy, QLabel, QFontDialog,
                             QMainWindow, QTextEdit, QAction, QFileDialog)
from PyQt5.QtGui import QColor, QIcon


class Example1(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('对话框', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('输入对话框')
        self.show()

    def showDialog(self):
        """
        第一个字符串参数是对话框的标题，第二个字符串参数是对话框内的消息文本。
        对话框返回输入的文本内容和一个布尔值。
        如果我们点击了Ok按钮，布尔值就是true，反之布尔值是false
        """
        text, ok = QInputDialog.getText(self, '输入对话框',
                                        '输入你的名字:')  # 这一行会显示一个输入对话框

        if ok:
            self.le.setText(str(text))  # 把我们从对话框接收到的文本设置到单行编辑框组件上显示。


class Example2(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)  # 初始化QtGuiQFrame组件的背景颜色

        self.btn = QPushButton('对话框', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('颜色对话框')
        self.show()

    def showDialog(self):
        """如果我们选中一个颜色并且点了ok按钮，会返回一个有效的颜色值。
        如果我们点击了Cancel按钮，不会返回选中的颜色值。我们使用样式表来定义背景颜色。
        """
        col = QColorDialog.getColor()  # 弹出颜色选择框

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())


class Example3(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('对话框', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
                          QSizePolicy.Fixed)

        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):
        """
        getFont()方法返回字体名字和布尔值。如果用户点击了OK，布尔值为True；否则为False。
        """
        font, ok = QFontDialog.getFont()  # 弹出一个字体对话框
        if ok:
            self.lbl.setFont(font)  # 如果我们点击了Ok按钮，标签字体会被改变


class Example4(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('koala.jpg'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        """
        第一个字符串参数是getOpenFileName()方法的标题。
        第二个字符串参数指定了对话框的工作目录。默认的，文件过滤器设置成All files (*)
        """
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')  # 弹出文件选择框

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)  # 选中文件后，读出文件的内容，并设置成文本编辑框组件的显示文本


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example4()
    sys.exit(app.exec_())
