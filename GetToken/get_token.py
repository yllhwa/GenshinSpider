# encoding:utf-8
import requests

ak = input("请输入百度提供的API Key:")
sk = input("请输入百度提供的Secret Key:")
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + \
    ak+'&client_secret='+sk
response = requests.get(host)
if response:
    print(response.json()['access_token'])
input()
