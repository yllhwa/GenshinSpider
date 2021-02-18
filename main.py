import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication
from mainwindow import mainwindow


def main():
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = mainwindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
