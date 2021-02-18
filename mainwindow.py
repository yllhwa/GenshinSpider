from Ui_MainWindow import Ui_MainWindow

import json
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from base64 import b64encode
from io import BytesIO
from xlrd import open_workbook
from xlutils.copy import copy

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
        artifact = get_stat(img, self.url, self.access_token)
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
        workbook = open_workbook(
            os.getcwd() + "\\output.xls", formatting_info=True)  # 打开工作簿
        sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
        worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
        rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
        new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格

        new_worksheet.write(rows_old, 0, output['name'])
        new_worksheet.write(rows_old, 1, output['kind'])
        new_worksheet.write(rows_old, 2, output['main_attr'])
        new_worksheet.write(rows_old, 3, output['main_attr_value'])
        new_worksheet.write(rows_old, 4, output['star'])
        new_worksheet.write(rows_old, 5, output['lv'])
        new_worksheet.write(rows_old, 6, output['vice1_attr'])
        new_worksheet.write(rows_old, 7, output['vice1_num'])
        new_worksheet.write(rows_old, 8, output['vice2_attr'])
        new_worksheet.write(rows_old, 9, output['vice2_num'])
        new_worksheet.write(rows_old, 10, output['vice3_attr'])
        new_worksheet.write(rows_old, 11, output['vice3_num'])
        new_worksheet.write(rows_old, 12, output['vice4_attr'])
        new_worksheet.write(rows_old, 13, output['vice4_num'])
        new_worksheet.write(rows_old, 14, output['set_name'])
        new_workbook.save(os.getcwd() + "\\output.xls")
