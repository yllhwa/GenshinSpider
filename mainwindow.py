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

    def set_text(self, artifact):
        """
        将圣遗物数据显示到界面上
        :param artifact: 圣遗物对象
        :return: None
        """
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

    def get_text(self):
        """
        获取界面上的圣遗物数据到字典
        :param: None
        :return: 圣遗物数据字典
        """
        output = {}
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
        access_token = "**********"
        artifact = get_stat(img, access_token)
        self.set_text(artifact)
        # self.window.showNormal()

    def on_save_btn_clicked(self):
        output = {}
        output = self.get_text()
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
