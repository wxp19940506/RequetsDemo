#-*- coding:utf-8 -*-
import requests

if __name__ == '__main__':
    response = requests.get("https://www.baidu.com/")
    # print(type(response.text))
    # print(response.text)
    # print(type(response.content))
    # print(response.content.decode('utf-8'))
    print(response.url)
    print(response.encoding)
    print(response.status_code)