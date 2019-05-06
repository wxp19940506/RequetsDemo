#-*- coding:utf-8 -*-
from urllib import request,parse

if __name__ == '__main__':
    # url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36 ',
    #     'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    # }
    # data = {
    #     'first':'true',
    #     'pn':1,
    #     'kd':'python'
    # }
    # req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
    # resp = request.urlopen(req)
    # print(resp.read().decode('utf-8'))



    def callbackfunc(blocknum, blocksize, totalsize):
        '''回调函数
        @blocknum: 已经下载的数据块
        @blocksize: 数据块的大小
        @totalsize: 远程文件的大小
        '''
        percent = 100.0 * blocknum * blocksize / totalsize
        if percent > 100:
            percent = 100
        print("%.2f%%" % percent)


    headers = [( 'User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36 '),
               ( 'Referer','https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=')]
    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'python'
    }
    opener =  request.build_opener()
    opener.addheaders = headers
    request.install_opener(opener)
    # request.urlretrieve(url,"lagou_python.json",reporthook=cbk)
    # request.urlretrieve(url,"lagou_python.json",data=parse.urlencode(data).encode('utf-8'),reporthook=callbackfunc)
    request.urlretrieve(url,"lagou.html",data=parse.urlencode(data).encode('utf-8'),reporthook=callbackfunc)


