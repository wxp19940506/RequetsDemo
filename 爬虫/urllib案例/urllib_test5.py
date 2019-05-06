#-*- coding:utf-8 -*-

from urllib import request
if __name__ == '__main__':

    # 不使用代理
    url = "http://httpbin.org/ip"
    resp = request.urlopen(url)
    print(resp.read())

    # 使用代理
    handler = request.ProxyHandler({'http':'123.56.151.10:9999'})
    opener = request.build_opener(handler)
    resp = opener.open(url)
    print(resp.read())