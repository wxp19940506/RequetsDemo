#-*- coding:utf-8 -*-

from urllib import parse,request
if __name__ == '__main__':
    params = {'name':'张三','age':19,'greet':'hello world'}
    result = parse.urlencode(params)
    print(result)
    print("-------------------------")
    params1 ={'wd':'刘德华'}
    qs = parse.urlencode(params1)
    url = "http://www.baidu.com/s?"+qs
    resp = request.urlopen(url)
    print(resp.read())
    print("-------------------------")
    params2 = {'name': '张三', 'age': 19, 'greet': 'hello world'}
    qs1 = parse.urlencode(params2)
    result1 = parse.parse_qs(qs1)
    print(result1)