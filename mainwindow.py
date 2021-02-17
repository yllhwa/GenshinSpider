import json
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

import base64
from io import BytesIO
from PIL import Image
import pandas as pd

from printScreen import print_screen
from utils import *


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(345, 312)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grab_btn = QtWidgets.QPushButton(self.centralwidget)
        self.grab_btn.setGeometry(QtCore.QRect(70, 270, 81, 31))
        self.grab_btn.setObjectName("grab_btn")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 251))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 301, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.star_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.star_label.setObjectName("star_label")
        self.gridLayout.addWidget(self.star_label, 2, 2, 1, 1)
        self.vice3_num_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.vice3_num_edit.setObjectName("vice3_num_edit")
        self.gridLayout.addWidget(self.vice3_num_edit, 8, 3, 1, 1)
        self.main_num_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.main_num_edit.setObjectName("main_num_edit")
        self.gridLayout.addWidget(self.main_num_edit, 5, 3, 1, 1)
        self.kind_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.kind_label.setObjectName("kind_label")
        self.gridLayout.addWidget(self.kind_label, 0, 2, 1, 1)
        self.vice3_attr_num = QtWidgets.QLabel(self.gridLayoutWidget)
        self.vice3_attr_num.setObjectName("vice3_attr_num")
        self.gridLayout.addWidget(self.vice3_attr_num, 8, 2, 1, 1)
        self.main_attr_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.main_attr_edit.setObjectName("main_attr_edit")
        self.gridLayout.addWidget(self.main_attr_edit, 5, 1, 1, 1)
        self.name_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name_edit.setObjectName("name_edit")
        self.gridLayout.addWidget(self.name_edit, 0, 1, 1, 1)
        self.level_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.level_label.setObjectName("level_label")
        self.gridLayout.addWidget(self.level_label, 4, 0, 1, 1)
        self.level_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.level_edit.setObjectName("level_edit")
        self.gridLayout.addWidget(self.level_edit, 4, 1, 1, 1)
        self.vice1_attr_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.vice1_attr_label.setObjectName("vice1_attr_label")
        self.gridLayout.addWidget(self.vice1_attr_label, 6, 0, 1, 1)
        self.set_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.set_label.setObjectName("set_label")
        self.gridLayout.addWidget(self.set_label, 2, 0, 1, 1)
        self.main_num_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_num_label.setObjectName("main_num_label")
        self.gridLayout.addWidget(self.main_num_label, 5, 2, 1, 1)
        self.kind_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.kind_edit.setObjectName("kind_edit")
        self.gridLayout.addWidget(self.kind_edit, 0, 3, 1, 1)
        self.vice1_attr_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.vice1_attr_edit.setObjectName("vice1_attr_edit")
        self.gridLayout.addWidget(self.vice1_attr_edit, 6, 1, 1, 1)
        self.vice2_attr_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.vice2_attr_label.setObjectName("vice2_attr_label")
        self.gridLayout.addWidget(self.vice2_attr_label, 7, 0, 1, 1)
        self.vice1_attr_num = QtWidgets.QLabel(self.gridLayoutWidget)
        self.vice1_attr_num.setObjectName("vice1_attr_num")
        self.gridLayout.addWidget(self.vice1_attr_num, 6, 2, 1, 1)
        self.main_attr_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.main_attr_label.setObjectName("main_attr_label")
        self.gridLayout.addWidget(self.main_attr_label, 5, 0, 1, 1)
        self.vice2_num_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.vice2_num_edit.setObjectName("vice2_num_edit")
        self.gridLayout.addWidget(self.vice2_num_edit, 7, 3, 1, 1)
        self.name_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.vice2_attr_num = QtWidgets.QLabel(self.gridLayoutWidget)
        self.vice2_attr_num.setObjectName("vice2_attr_num")
        self.gridLayout.addWidget(self.vice2_attr_num, 7, 2, 1, 1)
        self.vice3_attr_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.vice3_attr_label.setObjectName("vice3_attr_label")
        self.gridLayout.addWidget(self.vice3_attr_label, 8, 0, 1, 1)
        self.vice1_num_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.vice1_num_edit.setObjectName("vice1_num_edit")
        self.gridLayout.addWidget(self.vice1_num_edit, 6, 3, 1, 1)
        self.vice2_attr_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.vice2_attr_edit.setObjectName("vice2_attr_edit")
        self.gridLayout.addWidget(self.vice2_attr_edit, 7, 1, 1, 1)
        self.vice3_attr_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.vice3_attr_edit.setObjectName("vice3_attr_edit")
        self.gridLayout.addWidget(self.vice3_attr_edit, 8, 1, 1, 1)
        self.set_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.set_edit.setObjectName("set_edit")
        self.gridLayout.addWidget(self.set_edit, 2, 1, 1, 1)
        self.vice4_attr_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.vice4_attr_label.setObjectName("vice4_attr_label")
        self.gridLayout.addWidget(self.vice4_attr_label, 9, 0, 1, 1)
        self.vice4_attr_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.vice4_attr_edit.setObjectName("vice4_attr_edit")
        self.gridLayout.addWidget(self.vice4_attr_edit, 9, 1, 1, 1)
        self.vice4_attr_num = QtWidgets.QLabel(self.gridLayoutWidget)
        self.vice4_attr_num.setObjectName("vice4_attr_num")
        self.gridLayout.addWidget(self.vice4_attr_num, 9, 2, 1, 1)
        self.vice4_num_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.vice4_num_edit.setObjectName("vice4_num_edit")
        self.gridLayout.addWidget(self.vice4_num_edit, 9, 3, 1, 1)
        self.star_box = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.star_box.setObjectName("star_box")
        self.star_box.addItem("")
        self.star_box.addItem("")
        self.star_box.addItem("")
        self.star_box.addItem("")
        self.star_box.addItem("")
        self.gridLayout.addWidget(self.star_box, 2, 3, 1, 1)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(200, 270, 80, 31))
        self.save_btn.setObjectName("save_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.grab_btn.setText(_translate("MainWindow", "抓取"))
        self.groupBox.setTitle(_translate("MainWindow", "圣遗物信息"))
        self.star_label.setText(_translate("MainWindow", "星级"))
        self.kind_label.setText(_translate("MainWindow", "类型"))
        self.vice3_attr_num.setText(_translate("MainWindow", "数值"))
        self.level_label.setText(_translate("MainWindow", "等级"))
        self.vice1_attr_label.setText(_translate("MainWindow", "副属性1"))
        self.set_label.setText(_translate("MainWindow", "所属套装"))
        self.main_num_label.setText(_translate("MainWindow", "数值"))
        self.vice2_attr_label.setText(_translate("MainWindow", "副属性2"))
        self.vice1_attr_num.setText(_translate("MainWindow", "数值"))
        self.main_attr_label.setText(_translate("MainWindow", "主属性"))
        self.name_label.setText(_translate("MainWindow", "名称"))
        self.vice2_attr_num.setText(_translate("MainWindow", "数值"))
        self.vice3_attr_label.setText(_translate("MainWindow", "副属性3"))
        self.vice4_attr_label.setText(_translate("MainWindow", "副属性4"))
        self.vice4_attr_num.setText(_translate("MainWindow", "数值"))
        self.star_box.setCurrentText(_translate("MainWindow", "5"))
        self.star_box.setItemText(0, _translate("MainWindow", "5"))
        self.star_box.setItemText(1, _translate("MainWindow", "4"))
        self.star_box.setItemText(2, _translate("MainWindow", "3"))
        self.star_box.setItemText(3, _translate("MainWindow", "2"))
        self.star_box.setItemText(4, _translate("MainWindow", "1"))
        self.save_btn.setText(_translate("MainWindow", "保存"))

    def on_grab_btn_clicked(self):
        # self.window.showMinimized()
        img = print_screen()
        weight, height = img.size
        box = (weight*0.67, height*0.15, weight*0.936, height*0.846)
        img = img.crop(box)
        output_buffer = BytesIO()
        img.save(output_buffer, format='JPEG')
        byte_data = output_buffer.getvalue()
        img = base64.b64encode(byte_data)
        access_token = "********************"
        artifact = get_stat(img, access_token)
        self.name_edit.setText(artifact.name)
        self.kind_edit.setText(artifact.set_pieces)
        self.set_edit.setText(artifact.set_name)
        self.star_box.setCurrentText(str(artifact.star))
        self.level_edit.setText(str(artifact.lv))
        self.main_attr_edit.setText(artifact.main_stat)
        self.main_num_edit.setText(artifact.main_stat_value)
        self.vice1_attr_edit.setText(artifact.vice_stat0)
        self.vice1_num_edit.setText(artifact.vice_stat0_value)
        self.vice2_attr_edit.setText(artifact.vice_stat1)
        self.vice2_num_edit.setText(artifact.vice_stat1_value)
        self.vice3_attr_edit.setText(artifact.vice_stat2)
        self.vice3_num_edit.setText(artifact.vice_stat2_value)
        self.vice4_attr_edit.setText(artifact.vice_stat3)
        self.vice4_num_edit.setText(artifact.vice_stat3_value)
        # self.window.showNormal()

    def on_save_btn_clicked(self):
        output = {}
        output['name'] = self.name_edit.text()
        output['kind'] = self.kind_edit.text()
        output['set_name'] = self.set_edit.text()
        try:
            output['star'] = int(self.star_box.currentText())
            output['lv'] = int(self.level_edit.text())
        except:
            pass
        output['main_attr'] = self.main_attr_edit.text()
        output['main_attr_value'] = self.main_num_edit.text()
        output['vice1_attr'] = self.vice1_attr_edit.text()
        output['vice1_num'] = self.vice1_num_edit.text()
        output['vice2_attr'] = self.vice2_attr_edit.text()
        output['vice2_num'] = self.vice2_num_edit.text()
        output['vice3_attr'] = self.vice3_attr_edit.text()
        output['vice3_num'] = self.vice3_num_edit.text()
        output['vice4_attr'] = self.vice4_attr_edit.text()
        output['vice4_num'] = self.vice4_num_edit.text()
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(json.dumps(output, indent=4, ensure_ascii=False))
        self.add_to_excel(output)
        QMessageBox.about(self.window, "成功", "已经复制到剪贴板以及保存到excel")

    def add_to_excel(self, output):
        if not os.path.exists('输出.xlsx'):
            dic1 = {'圣遗物名称': [],
                    '圣遗物类型': [],
                    '主属性': [],
                    '主属性数值': [],
                    '星级': [],
                    '等级': [],
                    '副属性1': [],
                    '副属性1数值': [],
                    '副属性2': [],
                    '副属性2数值': [],
                    '副属性3': [],
                    '副属性3数值': [],
                    '副属性4': [],
                    '副属性4数值': [],
                    '所属套装': []
                    }
            df = pd.DataFrame(dic1)
            df.to_excel('输出.xlsx', index=False)
        sheet = pd.read_excel('输出.xlsx')
        insert_column = {'圣遗物名称': output['name'],
                         '圣遗物类型': output['kind'],
                         '主属性': output['main_attr'],
                         '主属性数值': output['main_attr_value'],
                         '星级': output['star'],
                         '等级': output['lv'],
                         '副属性1': output['vice1_attr'],
                         '副属性1数值': output['vice1_num'],
                         '副属性2': output['vice2_attr'],
                         '副属性2数值': output['vice2_num'],
                         '副属性3': output['vice3_attr'],
                         '副属性3数值': output['vice3_num'],
                         '副属性4': output['vice4_attr'],
                         '副属性4数值': output['vice4_num'],
                         '所属套装': output['set_name']
                         }
        sheet = sheet.append(insert_column, ignore_index=True)
        sheet.to_excel('输出.xlsx', index=False)
