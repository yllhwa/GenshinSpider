import os

from configparser import ConfigParser


def read_api_config():
    conn = ConfigParser()
    file_path = os.getcwd() + "\\config.ini"
    if not os.path.exists(file_path):
        raise FileNotFoundError("配置文件不存在")

    conn.read(file_path, encoding="utf-8")

    use = conn.get('api', 'use')
    url = conn.get('api', use)
    access_token = conn.get('api', 'access_token')

    return url, access_token


def read_grasp_setting():
    conn = ConfigParser()
    file_path = os.getcwd() + "\\config.ini"
    if not os.path.exists(file_path):
        raise FileNotFoundError("配置文件不存在")

    conn.read(file_path, encoding="utf-8")

    window_title = conn.get('grasp_setting', 'window_title')
    left = conn.get('grasp_setting', 'left')
    top = conn.get('grasp_setting', 'top')
    right = conn.get('grasp_setting', 'right')
    bottom = conn.get('grasp_setting', 'bottom')
    return window_title, float(left), float(top), float(right), float(bottom)
