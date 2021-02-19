from time import sleep

import win32api
import win32con
import win32gui
import win32print
from PIL import ImageGrab


def get_real_resolution():
    """获取真实的分辨率"""
    hDC = win32gui.GetDC(0)
    # 横向分辨率
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    # 纵向分辨率
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h


def get_screen_size():
    """获取缩放后的分辨率"""
    w = win32api.GetSystemMetrics(0)
    h = win32api.GetSystemMetrics(1)
    return w, h


def get_window_handle(name):
    handle = win32gui.FindWindow(0, name)
    if handle == 0:
        return None
    else:
        win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND,
                             win32con.SC_RESTORE, 0)
        win32gui.SetForegroundWindow(handle)
        return handle


def get_window_pos(handle):
    real_resolution = get_real_resolution()
    screen_size = get_screen_size()
    screen_scale_rate = round(real_resolution[0] / screen_size[0], 2)
    return [i * screen_scale_rate for i in win32gui.GetWindowRect(handle)]


def print_screen(window_title, left, top, right, bottom):
    handle = get_window_handle(window_title)
    while (win32gui.IsIconic(handle)):
        pass
    sleep(0.5)
    (x1, y1, x2, y2) = get_window_pos(handle)
    img = ImageGrab.grab((x1, y1, x2, y2))
    img.show()
    weight, height = img.size
    box = (weight*left, height*top, weight*right, height*bottom)
    img = img.crop(box)
    img.show()
    return img
