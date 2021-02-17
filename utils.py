from fuzzywuzzy.fuzz import partial_ratio
import requests
from math import sqrt


class Artifact:
    """
    圣遗物类
    """
    name = ''  # 圣遗物名称
    set_pieces = ''  # 圣遗物类型
    set_name = ''  # 所属套装
    star = 5  # 星级
    lv = 0  # 等级
    main_stat = ''  # 主属性
    main_stat_value = ''  # 主属性数值
    vice_stat0 = ''  # 副属性1
    vice_stat0_value = ''  # 副属性1数值
    vice_stat1 = ''  # 副属性2
    vice_stat1_value = ''  # 副属性2数值
    vice_stat2 = ''  # 副属性3
    vice_stat2_value = ''  # 副属性3数值
    vice_stat3 = ''  # 副属性4
    vice_stat3_value = ''  # 副属性4数值

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.__dict__)


def get_stat(img, access_token):
    """
    OCR获取数据写入到圣遗物对象
    :param img: base64格式图像
    :param access_token: 百度ai的文字识别token
    :return: 圣遗物对象
    """
    params = {"image": img}
    # 高精度和普通接口
    #request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    print(response.text)

    def get_set_list_index(result):
        """
        判断圣遗物套装所在位置
        :param result: OCR结果列表
        :return: int 表示位置
        """
        set_list = ['幸运儿', '游医', '冒险家', '学士', '战狂', '祭冰之人', '奇迹', '勇士之心', '教官', '祭火之人', '赌徒',
                    '祭水之人', '武人', '守护之心', '祭雷之人', '流放者', '行者之心', '炽烈的炎之魔女', '角斗士的终幕礼',
                    '如雷的盛怒', '冰风迷途的勇士', '染血的骑士道', '昔日宗室之仪', '沉沦之心', '悠古的磐岩',
                    '翠绿之影', '流浪大地的乐团', '逆飞的流星', '平息鸣雷的尊者', '渡过烈火的贤人', '被怜爱的少女']
        # loc = [i in set_list for i in result].index(True)
        for i in result:
            for j in set_list:
                if partial_ratio(i, j) > 80:  # 模糊字符串匹配
                    return result.index(i)

    def get_index(lst, item):
        return [index for (index, value) in enumerate(lst) if value == item]

    def get_vice_stat_index(result, set_loc):
        """
        判断圣遗物副词条所在位置
        :param result: OCR结果列表
        :return: int 表示位置
        """
        stat_list = ['治疗加成', '攻击力', '生命值', '防御力', '元素精通', '元素充能效率', '暴击率', '暴击伤害', '风元素伤害加成', '火元素伤害加成',
                     '水元素伤害加成', '雷元素伤害加成', '冰元素伤害加成', '岩元素伤害加成' '物理伤害加成']
        # loc = get_index([i.split('+')[0] in stat_list for i in result], True)[1:]
        loc = []
        ptr = 0
        for i in result[:set_loc]:
            for j in stat_list:
                if partial_ratio(i, j) > 80:
                    loc.append(ptr)
                    break
            ptr += 1
        return loc[1:]

    if response:
        result = response.json()['words_result']
        result = [str(i['words']).replace('·', '').replace(':', '').replace(',', '')
                  for i in result]
        artifact = Artifact(result[0])
        artifact.set_pieces = result[1]
        artifact.main_stat = result[2]
        artifact.main_stat_value = result[3]
        artifact.star = len(result[4])
        if result[5][0] == '+':
            artifact.lv = int(result[5])
        for item in result[5:]:
            if '+' in item:
                if artifact.vice_stat0 == '':
                    artifact.vice_stat0 = item.split('+')[0]
                    artifact.vice_stat0_value = str(item.split('+')[1])
                elif artifact.vice_stat1 == '':
                    artifact.vice_stat1 = item.split('+')[0]
                    artifact.vice_stat1_value = str(item.split('+')[1])
                elif artifact.vice_stat2 == '':
                    artifact.vice_stat2 = item.split('+')[0]
                    artifact.vice_stat2_value = str(item.split('+')[1])
                elif artifact.vice_stat3 == '':
                    artifact.vice_stat3 = item.split('+')[0]
                    artifact.vice_stat3_value = str(item.split('+')[1])
        set_list_index = get_set_list_index(result)
        artifact.set_name = result[set_list_index]
        return artifact
