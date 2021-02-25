import cv2
import numpy as np
import math


def pre_treat(img):
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度
    ret, thresh = cv2.threshold(imgray, 225, 255, 0)  # 二值化
    return thresh


def test_show(img):
    cv2.namedWindow("show", 0)
    cv2.imshow('show', img)
    cv2.waitKey(0)


def pre_screen(contours):
    target = []  # 保存预筛选矩形
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)  # 拟合矩形轮廓
        # 剔除太小的矩形
        if (w < 80):
            continue
        if (h < 35):
            continue
        #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 5)
        # 保留宽高比约为3的矩形到target
        if (w / h >= 2 and w / h <= 4):
            target.append({'x': x, 'y': y, 'w': w, 'h': h})
    return target


def arrange(target):
    detail = []  # 保存确定的矩形
    row = []  # 保存每一行

    # 将矩形结果分行
    row.append(target[-1])
    for item in target[-2::-1]:
        if abs(item['y'] - row[-1]['y']) < 50:
            row.append(item)
        else:
            detail.append([x for x in row])
            row.clear()
            row.append(item)
    if not row in detail:
        detail.append([x for x in row])

    # 剔除内容不足三个的行
    for row in detail[:]:
        if len(row) < 3:
            detail.remove(row)
    return detail


def get_border(detail):
    # 投票(取中位数)左边界\右边界\上边界\下边界
    left_x_list = []
    right_x_list = []
    up_y_list = []
    bottom_y_list = []
    for item in detail[0]:
        up_y_list.append(item['y'])
    for item in detail[-1]:
        bottom_y_list.append(item['y'])
    for row in detail:
        row.sort(key=(lambda item: item['x']))
        left_x_list.append(row[0]['x'])
        right_x_list.append(row[-1]['x'])
    left_x_list.sort()
    left_x = left_x_list[len(left_x_list) // 2]
    right_x_list.sort()
    right_x = right_x_list[len(right_x_list) // 2]
    up_y_list.sort()
    up_y = up_y_list[len(up_y_list) // 2]
    bottom_y_list.sort()
    bottom_y = bottom_y_list[len(bottom_y_list) // 2]
    return left_x, right_x, up_y, bottom_y


def process(img):
    thresh = pre_treat(img)  # 预处理

    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 寻找轮廓
    # test_show(contours)
    target = pre_screen(contours)  # 初筛选矩形
    detail = arrange(target)  # 整理矩形，分行、剔除不合理内容
    left_x, right_x, up_y, bottom_y = get_border(detail)  # 划分边界
    print(left_x, right_x, up_y, bottom_y)
    # 计算每个的间隔
    aver_x = (right_x - left_x) / 6  # 7个圣遗物6个空格
    aver_y = (bottom_y - up_y) / (len(detail) - 1)
    # 统计矩形的平均宽高
    aver_w = detail[0][0]['w']
    aver_h = detail[0][0]['h']
    all_count = 0
    for row in detail:
        for item in row:
            aver_w += item['w']
            aver_h += item['h']
            all_count += 1
    aver_w /= all_count
    aver_h /= all_count

    out_detail = []
    test_img = img
    # 画出矩形
    for row in range(0, len(detail)):
        out_row = []
        for item in range(0, 7):
            out_row.append({'x': int(left_x+aver_x*item+aver_w/2),
                            'y': int(up_y+aver_y*row)})
            #cv2.rectangle(test_img, (int(left_x+aver_x*item), int(up_y+aver_y*row)), (int(left_x + aver_x * item + aver_w), int(up_y + aver_y * row + aver_h)), (0, 255, 0), 5)
        out_detail.append(out_row)
    return out_detail


def test():
    img = cv2.imread('./test1.jpg')  # 传入图片
    detail = process(img)

    for row in detail:
        for item in row:
            cv2.circle(img, (item['x'], item['y']), 20, (0, 0, 255), -1)
    cv2.imwrite('./test7_ok.png', img)


if __name__ == "__main__":
    test()
