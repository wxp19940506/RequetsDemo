#-*- coding:utf-8 -*-
from urllib import request
from http.cookiejar import MozillaCookieJar

if __name__ == '__main__':
    url = 'http://www.baidu.com/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36',
    }
    # 保存cookie到本地
    cookiejar = MozillaCookieJar('cookie.txt')
    # 从本地加载cookie
    # cookiejar.load(ignore_discard=True)
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)
    # resp = opener.open(url)
    print('----------------------')
    url_bin = "http://httpbin.org/cookies/set?course=abc"
    resp = opener.open(url_bin)
    # cookiejar.save(ignore_discard=True)
    for cookie in cookiejar:
        print(cookie)