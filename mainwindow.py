from Ui_MainWindow import Ui_MainWindow

import json
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from base64 import b64encode
from io import BytesIO
from pandas import DataFrame, read_excel

from printScreen import print_screen
from utils import *


class mainwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.window = QtWidgets.QMainWindow()
        self.setupUi(self)
        self.setWindowTitle("原神数据抓取器")
        self.move(0, 0)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)  # 置顶
        self.grab_btn.clicked.connect(self.on_grab_btn_clicked)
        self.save_btn.clicked.connect(self.on_save_btn_clicked)

<<<<<<< HEAD
    def set_text(self, artifact):
=======
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
        access_token = "*********************"
        artifact = get_stat(img, access_token)
>>>>>>> 95307e2555f99021d9684a41f0a5cd39176c0884
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

    def get_text(self, output):
        try:
            output['name'] = self.name_edit.text()
            output['kind'] = self.kind_edit.text()
            output['set_name'] = self.set_edit.text()
            output['star'] = int(self.star_box.currentText())
            output['lv'] = int(self.level_edit.text())
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
        except:
            pass
        return output

    def on_grab_btn_clicked(self):
        # self.window.showMinimized()
        img = print_screen()
        output_buffer = BytesIO()
        img.save(output_buffer, format='JPEG')
        byte_data = output_buffer.getvalue()
        img = b64encode(byte_data)
        access_token = "***********"
        artifact = get_stat(img, access_token)
        self.set_text(artifact)
        # self.window.showNormal()

    def on_save_btn_clicked(self):
        output = {}
        output = self.get_text(output)
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(json.dumps(output, indent=4, ensure_ascii=False))
        self.add_to_excel(output)
        QMessageBox.about(self, "成功", "已经复制到剪贴板以及保存到excel")

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
            df = DataFrame(dic1)
            df.to_excel('输出.xlsx', index=False)
        sheet = read_excel('输出.xlsx')
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
