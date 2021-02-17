from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from mainwindow import mainwindow


def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    win = mainwindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
