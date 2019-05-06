#-*- coding:utf-8 -*-

from urllib import request,parse
from http.cookiejar import CookieJar


headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36',
    }

def get_opener():
    # 1.登录
    # 1.1创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2使用cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3使用上一步创建的handler创建opener
    opener = request.build_opener(handler)
    return opener


def login_renren(opener):
    # 1.4使用opener发送登录的请求（人人网邮箱和密码）

    data = {
        'email': '2376333613@qq.com',
        'password': 'Trvqd@123'
    }
    login_url = 'http://www.renren.com/PLogin.do'
    req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
    opener.open(req)

def visit_profile(opener):
    # 2.访问个人主页
    denglu_url = 'http://www.renren.com/967687907/profile'
    # 获取个人主页的时候，不需要再建一个opener
    # 而应该使用之前的opener对象，因为其包含了登录后的cookie
    req = request.Request(denglu_url,headers=headers)
    resp = opener.open(req)
    with open('renren.html','w',encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)