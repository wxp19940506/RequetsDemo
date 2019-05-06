#-*- coding:utf-8 -*-
import requests
if __name__ == '__main__':
    response = requests.get('https://www.12306.com',verify=False)
    print(response.content.decode('utf-8'))