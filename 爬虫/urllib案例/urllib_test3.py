#-*- coding:utf-8 -*-
from  urllib import parse

if __name__ == '__main__':
    url = "http://www.baidu.com/s?wd=python&username=abc#1"
    # result = parse.urlparse(url)
    result = parse.urlsplit(url)
    print(result)
    print(result.scheme)
    print(result.netloc)
    print(result.path)
    # print(result.params)
    print(result.query)
    print(result.fragment)