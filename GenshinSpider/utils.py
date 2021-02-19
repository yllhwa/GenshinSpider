from requests import post

from fuzzywuzzy.fuzz import partial_ratio


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


def get_name(kind, name):
    kind_list = ["生之花", "死之羽", "时之沙", "空之杯", "理之冠"]
    name_list = {
        "生之花": ["饰金胸花", "历经风雪的思念", "磐陀裂生之花", "夏祭之花", "游医的银莲", "赌徒的胸花", "学士的书签", "染血的铁之心", "勇士的勋章", "武人的红花", "角斗士的留恋", "教官的胸花", "宗室之花", "守护之花",
                "野花记忆的绿野", "流放者之花", "渡火者的决绝", "乐团的晨光", "远方的少女之心", "魔女的炎之花", "雷鸟的怜悯", "战狂的蔷薇", "平雷之心", "奇迹之花", "故人之心", "幸运儿绿花", "冒险家之花"],
        "死之羽": ["摧冰而行的执望", "追忆之风", "嵯峨群峰之翼", "夏祭终末", "游医的枭羽", "赌徒的羽饰", "学士的羽笔", "染血的黑之羽", "流放者之羽", "琴师的箭羽", "守护徽印", "勇士的期许", "武人的羽饰", "宗室之翎",
                "角斗士的归宿", "猎人青翠的箭羽", "少女飘摇的思念", "魔女常燃之羽", "教官的羽饰", "雷灾的孑遗", "渡火者的解脱", "战狂的翎羽", "平雷之羽", "奇迹之羽", "归乡之羽", "幸运儿鹰羽", "冒险家尾羽"],
        "时之沙": ["坚铜罗盘", "冰雪故园的终期", "星罗圭璧之晷", "夏祭之刻", "游医的怀钟", "赌徒的怀表", "学士的时钟", "骑士染血之时", "流放者怀表", "教官的怀表", "终幕的时计", "勇士的坚毅", "守护座钟", "武人的水漏",
                "角斗士的希冀", "翠绿猎人的笃定", "渡火者的煎熬", "宗室时计", "少女苦短的良辰", "魔女破灭之时", "雷霆的时计", "战狂的时计", "平雷之刻", "奇迹之沙", "逐光之石", "幸运儿沙漏", "冒险家怀表"],
        "空之杯": ["沉波之盏", "遍结寒霜的傲骨", "巉岩琢塑之樽", "夏祭水玉", "游医的药壶", "赌徒的骰盅", "学士的墨杯", "染血骑士之杯", "流放者之杯", "守护之皿", "吟游者之壶", "勇士的壮行", "角斗士的酣醉", "宗室银瓮",
                "翠绿猎人的容器", "战狂的骨杯", "少女片刻的闲暇", "魔女的心之火", "教官的茶杯", "降雷的凶兆", "渡火者的醒悟", "平雷之器", "武人的酒杯", "奇迹之杯", "异国之盏", "幸运儿之杯", "冒险家金杯"],
        "理之冠": ["酒渍船帽", "破冰踏雪的回音", "不动玄石之相", "夏祭之面", "祭雷礼冠", "祭火礼冠", "祭水礼冠", "祭冰礼冠", "游医的方巾", "学士的镜片", "赌徒的耳环", "染血的铁假面", "渡火者的智慧", "流放者头冠", "宗室面具", "勇士的冠冕",
                "守护束带", "武人的头巾", "角斗士的凯旋", "翠绿的猎人之冠", "指挥的礼帽", "焦灼的魔女帽", "教官的帽子", "唤雷的头冠", "战狂的鬼面", "平雷之冠", "少女易逝的芳颜", "奇迹耳坠", "感别之冠", "幸运儿银冠", "冒险家头带"]
    }
    out_name = ''
    max = 0
    for set_name in name_list[kind]:
        ratio = partial_ratio(set_name, name)
        if ratio > max:
            max = ratio
            out_name = set_name
    return out_name


def get_kind(kind):
    kind_list = ["生之花", "死之羽", "时之沙", "空之杯", "理之冠"]
    for set_kind in kind_list:
        if partial_ratio(set_kind, kind) > 80:
            return set_kind


def get_set_name(result):
    set_list = ['幸运儿', '游医', '冒险家', '学士', '战狂', '祭冰之人', '奇迹', '勇士之心', '教官', '祭火之人', '赌徒',
                '祭水之人', '武人', '守护之心', '祭雷之人', '流放者', '行者之心', '炽烈的炎之魔女', '角斗士的终幕礼',
                '如雷的盛怒', '冰风迷途的勇士', '染血的骑士道', '昔日宗室之仪', '沉沦之心', '悠古的磐岩',
                '翠绿之影', '流浪大地的乐团', '逆飞的流星', '平息鸣雷的尊者', '渡过烈火的贤人', '被怜爱的少女']
    # loc = [i in set_list for i in result].index(True)
    for i in result:
        for j in set_list:
            if partial_ratio(i, j) > 80:  # 模糊字符串匹配
                return j


def get_stat(img, request_url, access_token):
    """
    OCR获取数据写入到圣遗物对象
    :param img: base64格式图像
    :param access_token: 百度ai的文字识别token
    :return: 圣遗物对象
    """
    params = {"image": img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = post(request_url, data=params, headers=headers)
    # print(response.text)

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
        artifact.set_pieces = get_kind(result[1])
        artifact.name = get_name(artifact.set_pieces, result[0])
        artifact.main_stat = result[2]
        artifact.main_stat_value = result[3]
        if '%' in artifact.main_stat_value and artifact.main_stat_value[-3] != '.':
            print(artifact.main_stat_value[-3])
            str_list = list(artifact.main_stat_value)
            str_list.insert(-2, '.')
            artifact.main_stat_value = "".join(str_list)
        elif '.' in artifact.main_stat_value and artifact.main_stat_value[-1] != '%':
            print(artifact.main_stat_value[-1])
            str_list = list(artifact.main_stat_value)
            str_list.append('%')
            artifact.main_stat_value = "".join(str_list)
        artifact.star = len(result[4])
        if result[5][0] == '+':
            artifact.lv = int(result[5])
        # 下面的代码是屎山，是由历史遗留问题(变量名)产生的，有时间再重构，先跑起来
        for item in result[5:]:
            if '+' in item:
                if artifact.vice_stat0 == '':
                    artifact.vice_stat0 = item.split('+')[0]
                    artifact.vice_stat0_value = str(item.split('+')[1])
                    if '%' in artifact.vice_stat0_value and artifact.vice_stat0_value[-3] != '.':
                        str_list = list(artifact.vice_stat0_value)
                        str_list.insert(-2, '.')
                        artifact.vice_stat0_value = "".join(str_list)
                    if artifact.vice_stat0_value == '7':
                        artifact.vice_stat0_value = '17'
                    if artifact.vice_stat0_value == '1':
                        artifact.vice_stat0_value = '11'
                elif artifact.vice_stat1 == '':
                    artifact.vice_stat1 = item.split('+')[0]
                    artifact.vice_stat1_value = str(item.split('+')[1])
                    if '%' in artifact.vice_stat1_value and artifact.vice_stat1_value[-3] != '.':
                        str_list = list(artifact.vice_stat1_value)
                        str_list.insert(-2, '.')
                        artifact.vice_stat1_value = "".join(str_list)
                    if artifact.vice_stat1_value == '7':
                        artifact.vice_stat1_value = '17'
                    if artifact.vice_stat1_value == '1':
                        artifact.vice_stat1_value = '11'
                elif artifact.vice_stat2 == '':
                    artifact.vice_stat2 = item.split('+')[0]
                    artifact.vice_stat2_value = str(item.split('+')[1])
                    if '%' in artifact.vice_stat2_value and artifact.vice_stat2_value[-3] != '.':
                        str_list = list(artifact.vice_stat2_value)
                        str_list.insert(-2, '.')
                        artifact.vice_stat2_value = "".join(str_list)
                    if artifact.vice_stat2_value == '7':
                        artifact.vice_stat2_value = '17'
                    if artifact.vice_stat2_value == '1':
                        artifact.vice_stat2_value = '11'
                elif artifact.vice_stat3 == '':
                    artifact.vice_stat3 = item.split('+')[0]
                    artifact.vice_stat3_value = str(item.split('+')[1])
                    if '%' in artifact.vice_stat3_value and artifact.vice_stat3_value[-3] != '.':
                        str_list = list(artifact.vice_stat3_value)
                        str_list.insert(-2, '.')
                        artifact.vice_stat3_value = "".join(str_list)
                    if artifact.vice_stat3_value == '7':
                        artifact.vice_stat3_value = '17'
                    if artifact.vice_stat3_value == '1':
                        artifact.vice_stat3_value = '11'
        set_list_index = get_set_list_index(result)
        artifact.set_name = get_set_name(result)
        return artifact
