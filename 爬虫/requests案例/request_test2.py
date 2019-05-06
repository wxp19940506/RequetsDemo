#-*- coding:utf-8 -*-
import requests
if __name__ == '__main__':
    url = "https://www.baidu.com/s"
    params = {
        'wd':'中国'
    }
    headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36',
    }
    response = requests.get(url,params=params,headers=headers)
    with open("zg.html",'w',encoding='utf-8') as fp:
        fp.write(response.content.decode('utf-8'))
    print(response.url)

