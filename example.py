# -*- coding: utf-8 -*-
"""在这个例子中, 我们用PyQt5创建了一个简单的窗口"""
__author__ = 'Huang Lun'
import sys
from PyQt5 import QtWidgets as qw
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication


class Example(qw.QMainWindow):

    def __init__(self):
        super().__init__()  # 继承父类QMainWindow的构造
        self.initUI()  # 自定义一个界面的UI显示方法

    def initUI(self):

        # 创建了一个文本编辑框组件。我们将它设置成QMainWindow的中心组件。
        # 中心组件占据了所有剩下的空间。
        textEdit = qw.QTextEdit()
        self.setCentralWidget(textEdit)

        # 创建了一个有指定图标和文本为'Exit'的标签。另外，还为这个动作定义了一个快捷键。
        # 第三行创建一个当我们鼠标浮于菜单项之上就会显示的一个状态提示。
        exitAction = qw.QAction(QIcon('koala.jpg'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')

        # 当我们选中特定的动作，一个触发信号会被发射。
        # 信号连接到QApplication组件的quit()方法，这样就中断了应用
        exitAction.triggered.connect(self.close)

        # 我们创建了一个工具栏，并且在其中插入一个动作对象
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.statusBar()  # 获得状态栏

        # menuBar()方法创建了一个菜单栏。
        # 我们创建一个file菜单，然后将退出动作添加到file菜单中
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        # 提示气泡和提示文本
        qw.QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 按钮和按钮提示气泡文本
        # btn = qw.QPushButton('Quit', self)
        # btn.clicked.connect(QCoreApplication.instance().quit)  # 按钮接受点击事件
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.resize(btn.sizeHint())  # 默认按钮大小
        # btn.move(50, 50)  # 按钮位置

        self.resize(250, 150)  # 窗口尺寸
        self.center()  # 自写的center方法使窗口居中显示
        self.setWindowTitle('Example')  # 窗口标题
        self.setWindowIcon(QIcon('koala.jpg'))  # 窗口图标
        self.show()  # 显示窗口

    def center(self):
        qr = self.frameGeometry()  # 获得屏幕矩形，包含窗口框架
        cp = qw.QDesktopWidget().availableGeometry().center()  # 计算相对于显示器的屏幕中心点
        qr.moveCenter(cp)  # 将矩形的中心设置到屏幕的中间去，矩形的大小并不会改变
        self.move(qr.topLeft())  # 移动应用窗口的左上方的点到qr矩形的左上方的点，因此居中显示在我们的屏幕上

    def closeEvent(self, event):
        """
        我们实现一个带两个按钮的message box：YES和No按钮。
        代码中第一个字符串的内容被显示在标题栏上。第二个字符串是对话框上显示的文本。
        第三个参数指定了显示在对话框上的按钮集合。最后一个参数是默认选中的按钮。
        这个按钮一开始就获得焦点。返回值被储存在reply变量中
        """
        reply = qw.QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                        qw.QMessageBox.Yes | qw.QMessageBox.No,
                                        qw.QMessageBox.No)
        if reply == qw.QMessageBox.Yes:
            event.accept()  # 接收事件
        else:
            event.ignore()  # 忽略事件


if __name__ == '__main__':
    app = qw.QApplication(sys.argv)  # 创建一个应用（Application）对象,sys.argv参数是一个来自命令行的参数列表
    ex = Example()

    # sys.exit()方法确保一个不留垃圾的退出,系统环境将会被通知应用是怎样被结束的
    # exec_()方法有一个下划线,因为exec是Python保留关键字,因此，用exec_()来代替
    sys.exit(app.exec_())
