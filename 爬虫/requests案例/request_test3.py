#-*- coding:utf-8 -*-
import requests
if __name__ == '__main__':
    url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    data = {
        'first':'true',
        'pn':'1',
        'kd':'python'
    }
    headers = {
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36',

    }
    response = requests.post(url,data=data,headers=headers)
    # print(response.json())
    print(type(response.json()))