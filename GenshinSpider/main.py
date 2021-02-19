import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox

from mainwindow import mainwindow
from readConfig import read_api_config, read_grasp_setting


def main():
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = mainwindow()
    try:
        win.url, win.access_token = read_api_config()
        win.window_title, win.left, win.top, win.right, win.bottom = read_grasp_setting()
    except:
        QMessageBox.warning(win, "失败", "读取配置文件失败")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
