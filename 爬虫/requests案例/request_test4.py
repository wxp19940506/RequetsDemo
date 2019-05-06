#-*- coding:utf-8 -*-
import requests
if __name__ == '__main__':
    url = 'http://httpbin.org/ip'
    proxy ={
        'http':'114.95.164.41:8060'
    }
    response = requests.get(url,proxies=proxy)
    print(response.text)