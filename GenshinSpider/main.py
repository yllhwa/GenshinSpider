import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from mainwindow import mainwindow

from readConfig import read_config


def main():
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = mainwindow()
    try:
        win.url, win.access_token = read_config()
    except:
        QMessageBox.warning(win, "失败", "读取配置文件失败")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
