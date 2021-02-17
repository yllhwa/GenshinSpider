from PyQt5 import QtCore, QtGui, QtWidgets
import sys


from mainwindow import Ui_MainWindow


def set_up_window(mainwindow, ui):
    ui.setupUi(mainwindow)
    ui.window = mainwindow
    mainwindow.setWindowTitle("原神数据抓取器")
    mainwindow.move(0, 0)
    mainwindow.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)  # 置顶
    # mainwindow.setWindowFlags(QtCore.Qt.Widget)  # 取消置顶
    ui.grab_btn.clicked.connect(ui.on_grab_btn_clicked)
    ui.save_btn.clicked.connect(ui.on_save_btn_clicked)
    mainwindow.show()


def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    set_up_window(mainwindow, ui)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
