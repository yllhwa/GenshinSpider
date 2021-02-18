import os

from configparser import ConfigParser


def read_config():
    conn = ConfigParser()
    file_path = os.getcwd() + "\\config.ini"
    if not os.path.exists(file_path):
        raise FileNotFoundError("配置文件不存在")

    conn.read(file_path)
    use = conn.get('api', 'use')
    url = conn.get('api', use)
    access_token = conn.get('api', 'access_token')
    return url, access_token
