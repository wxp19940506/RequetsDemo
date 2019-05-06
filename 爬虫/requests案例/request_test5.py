#-*- coding:utf-8 -*-
import requests
if __name__ == '__main__':
    # response= requests.get('https://www.baidu.com/')
    # print(response.cookies.get_dict())
    login_url = 'http://www.renren.com/PLogin.do'
    denglu_url = 'http://www.renren.com/967687907/profile'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36',
    }
    data = {
        'email': '2376333613@qq.com',
        'password': 'Trvqd@123'
    }
    session = requests.session()
    session.post(login_url,data=data,headers=headers)
    response = session.get(denglu_url)
    with open("renren.html",'w',encoding='utf-8') as fp:
        fp.write(response.text)

