import sys
import os
import json
from base64 import b64encode
from io import BytesIO

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from xlrd import open_workbook
from xlutils.copy import copy

from Ui_MainWindow import Ui_MainWindow
from printScreen import print_screen
from utils import *

set_name_translation = {
    "悠古的磐岩": "archaicPetra",
    "沉沦之心": "heartOfDepth",
    "冰风迷途的勇士": "blizzardStrayer",
    "逆飞的流星": "retracingBolide",
    "昔日宗室之仪": "noblesseOblige",
    "角斗士的终幕礼": "gladiatorFinale",
    "被怜爱的少女": "maidenBeloved",
    "翠绿之影": "viridescentVenerer",
    "渡过烈火的贤人": "lavaWalker",
    "炽烈的炎之魔女": "crimsonWitch",
    "平息雷鸣的尊者": "thunderSmoother",
    "如雷的盛怒": "thunderingFury",
    "染血的骑士道": "bloodstainedChivalry",
    "流浪大地的乐团": "wandererTroupe",
    "学士": "scholar",
    "赌徒": "gambler",
    "奇迹": "tinyMiracle",
    "武人": "martialArtist",
    "勇士之心": "braveHeart",
    "行者之心": "resolutionOfSojourner",
    "守护之心": "defenderWill",
    "战狂": "berserker",
    "教官": "instructor",
    "流放者": "exile",
    "冒险家": "adventurer",
    "幸运儿": "luckyDog",
    "游医": "travelingDoctor",
    "祭雷之人": "prayersForWisdom",
    "祭冰之人": "prayersToSpringtime",
    "祭火之人": "prayersForIllumination",
    "祭水之人": "prayersForDestiny"
}
kind_translation = {
    "生之花": "flower",
    "死之羽": "feather",
    "时之沙": "sand",
    "空之杯": "cup",
    "理之冠": "head"
}
Tag_name_translation = {
    "治疗效果": "cureEffect",
    "生命值": "life",
    "攻击力": "attack",
    "防御力": "defend",
    "暴击率": "critical",
    "暴击伤害": "criticalDamage",
    "元素精通": "elementalMastery",
    "元素充能效率": "recharge",
    "雷元素伤害加成": "thunderBonus",
    "火元素伤害加成": "fireBonus",
    "水元素伤害加成": "waterBonus",
    "冰元素伤害加成": "iceBonus",
    "风元素伤害加成": "windBonus",
    "岩元素伤害加成": "rockBonus",
    "物理伤害加成": "physicalBonus",
    "伤害加成": "bonus",
    "平A伤害加成": "aBonus",
    "重击伤害加成": "bBonus",
    "E伤害加成": "eBonus",
    "Q伤害加成": "qBonus"
    # Static
    # Percentage
}


class mainwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    json_dict = {"flower": [], "feather": [],
                 "sand": [], "cup": [], "head": []}
    id = 0

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
        try:
            img = print_screen(self.window_title, self.left,
                               self.top, self.right, self.bottom)
        except:
            QMessageBox.warning(self, "失败", "截取"+self.window_title+"窗口失败")
            return
        output_buffer = BytesIO()
        img.save(output_buffer, format='JPEG')
        byte_data = output_buffer.getvalue()
        img = b64encode(byte_data)
        try:
            artifact = get_stat(img, self.url, self.access_token)
        except:
            QMessageBox.warning(self, "出错", "识别圣遗物出错")
            return
        self.set_text(artifact)
        QMessageBox.about(self, "成功", "已成功抓取")

    def on_save_btn_clicked(self):
        output = {}
        output = self.get_text()
        try:
            single_artifact = {}
            single_artifact["setName"] = set_name_translation[output["set_name"]]
            single_artifact["detailName"] = output["name"]
            single_artifact["position"] = kind_translation[output["kind"]]
            mainTag = {"name": "", "value": ""}
            if "生命值" == output["main_attr"] or "攻击力" == output["main_attr"] or "防御力" == output["main_attr"]:
                if "%" in output["main_attr_value"]:
                    mainTag["name"] = Tag_name_translation[output["main_attr"]
                                                        ] + "Percentage"
                    mainTag["value"] = float(
                        output["main_attr_value"].replace("%", ""))/100
                else:
                    mainTag["name"] = Tag_name_translation[output["main_attr"]
                                                        ] + "Static"
                    mainTag["value"] = float(output["main_attr_value"])
            else:
                mainTag["name"] = Tag_name_translation[output["main_attr"]]
                if "%" in output["main_attr_value"]:
                    mainTag["value"] = float(
                        output["main_attr_value"].replace("%", "")) / 100
                else:
                    mainTag["value"] = float(output["main_attr_value"])
            single_artifact["mainTag"] = mainTag

            normalTags = []
            if(output["vice1_attr"]):
                vice1 = {"name": "", "value": ""}
                # vice1
                if "生命值" == output["vice1_attr"] or "攻击力" == output["vice1_attr"] or "防御力" == output["vice1_attr"]:
                    if "%" in output["vice1_num"]:
                        vice1["name"] = Tag_name_translation[output["vice1_attr"]
                                                            ] + "Percentage"
                        vice1["value"] = float(
                            output["vice1_num"].replace("%", ""))/100
                    else:
                        vice1["name"] = Tag_name_translation[output["vice1_attr"]
                                                            ] + "Static"
                        vice1["value"] = float(output["vice1_num"])
                else:
                    vice1["name"] = Tag_name_translation[output["vice1_attr"]]
                    if "%" in output["vice1_num"]:
                        vice1["value"] = float(
                            output["vice1_num"].replace("%", "")) / 100
                    else:
                        vice1["value"] = float(output["vice1_num"])
                normalTags.append(vice1)
            # vice2
            if(output["vice2_attr"]):
                vice2 = {"name": "", "value": ""}
                if "生命值" == output["vice2_attr"] or "攻击力" == output["vice2_attr"] or "防御力" == output["vice2_attr"]:
                    if "%" in output["vice2_num"]:
                        vice2["name"] = Tag_name_translation[output["vice2_attr"]
                                                            ] + "Percentage"
                        vice2["value"] = float(
                            output["vice2_num"].replace("%", ""))/100
                    else:
                        vice2["name"] = Tag_name_translation[output["vice2_attr"]
                                                            ] + "Static"
                        vice2["value"] = float(output["vice2_num"])
                else:
                    vice2["name"] = Tag_name_translation[output["vice2_attr"]]
                    if "%" in output["vice2_num"]:
                        vice2["value"] = float(
                            output["vice2_num"].replace("%", "")) / 100
                    else:
                        vice2["value"] = float(output["vice2_num"])
                normalTags.append(vice2)

            # vice3
            if(output["vice3_attr"]):
                vice3 = {"name": "", "value": ""}
                if "生命值" == output["vice3_attr"] or "攻击力" == output["vice3_attr"] or "防御力" == output["vice3_attr"]:
                    if "%" in output["vice3_num"]:
                        vice3["name"] = Tag_name_translation[output["vice3_attr"]
                                                            ] + "Percentage"
                        vice3["value"] = float(
                            output["vice3_num"].replace("%", ""))/100
                    else:
                        vice3["name"] = Tag_name_translation[output["vice3_attr"]
                                                            ] + "Static"
                        vice3["value"] = float(output["vice3_num"])
                else:
                    vice3["name"] = Tag_name_translation[output["vice3_attr"]]
                    if "%" in output["vice3_num"]:
                        vice3["value"] = float(
                            output["vice3_num"].replace("%", "")) / 100
                    else:
                        vice3["value"] = float(output["vice3_num"])
                normalTags.append(vice3)

            # vice4
            if(output["vice4_attr"]):
                vice4 = {"name": "", "value": ""}
                if "生命值" == output["vice4_attr"] or "攻击力" == output["vice4_attr"] or "防御力" == output["vice4_attr"]:
                    if "%" in output["vice4_num"]:
                        vice4["name"] = Tag_name_translation[output["vice4_attr"]
                                                            ] + "Percentage"
                        vice4["value"] = float(
                            output["vice4_num"].replace("%", ""))/100
                    else:
                        vice4["name"] = Tag_name_translation[output["vice4_attr"]
                                                            ] + "Static"
                        vice4["value"] = float(output["vice4_num"])
                else:
                    vice4["name"] = Tag_name_translation[output["vice4_attr"]]
                    if "%" in output["vice4_num"]:
                        vice4["value"] = float(
                            output["vice4_num"].replace("%", "")) / 100
                    else:
                        vice4["value"] = float(output["vice4_num"])
                normalTags.append(vice4)

            single_artifact["normalTags"] = normalTags
            single_artifact["omit"] = False
            single_artifact["id"] = hash(json.dumps(single_artifact))
            print(single_artifact)
            self.json_dict[kind_translation[output["kind"]]].append(
                single_artifact)
            clipboard = QtWidgets.QApplication.clipboard()
            clipboard.setText(json.dumps(
                self.json_dict, ensure_ascii=False))
        except:
            QMessageBox.warning(self, "出错", "复制到剪贴板出错")
        try:
            self.add_to_excel(output)
        except:
            QMessageBox.warning(self, "出错", "保存到excel出错")
            return
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
