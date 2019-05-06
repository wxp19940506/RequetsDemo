#-*- coding:utf-8 -*-
import requests

if __name__ == '__main__':
    #je8v
    url = "https://pan.baidu.com/s/1C2Y5UDXqkERx-AWHETlf3g#list/path=%2F"
    headers = {
        'Accept':'*/*',
        'Accept-Language':'zh-CN',
        'Cache-Control':'Keep-Alive',
        'Host':'pan.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36',
    }
    response = requests.get(url,headers=headers)
    with open("pan.html",'w',encoding='utf-8') as fp:
        fp.write(response.content.decode('utf-8'))
    print(response.url)
    print(response.content)
    print(response.status_code)