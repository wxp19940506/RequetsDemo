#-*- coding:utf-8 -*-
from urllib import request


if __name__ == '__main__':
    # resp = request.urlopen("http://www.baidu.com")
    # print(resp.read())
    # print(resp.getcode())
    # print(resp.read(200))
    # print(resp.read(200))
    # 下载网页
    # request.urlretrieve("http://www.baidu.com/","baidu.html")
    # 下载图片
    # request.urlretrieve("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1542711485481&di=182cb528130c9d104ab6a22e9988796b&imgtype=0&src=http%3A%2F%2Fimg3.redocn.com%2Ftupian%2F20140910%2Fxingganyouximeinvzhaopian_3014685.jpg","meinv.jpg")
    #http://tv.cctv.com/v/v1/VIDE7WE38U13X7VSnY2tO1uT180312.html
    # request.urlretrieve("http://tv.cctv.com/v/v1/VIDE7WE38U13X7VSnY2tO1uT180312.html","vod.html")
    # request.urlretrieve("http://tv.cctv.com/live/cctv3/","live.html")
    # request.urlretrieve("http://localhost:8080/dynamic_lib/index.html?_ijt=m645pobftbmtsiq2g69bm1830v","test.html")
    request.urlretrieve("https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=","lagou.html")
