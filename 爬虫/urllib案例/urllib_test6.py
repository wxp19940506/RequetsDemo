#-*- coding:utf-8 -*-

from  urllib import request

if __name__ == '__main__':
    url = "http://www.renren.com/967687907/profile"
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36',
        'Cookie':'anonymid=joquzpic2tajy8; __utma=151146938.1892114639.1542786069.1542786069.1542786069.1; __utmc=151146938; __utmz=151146938.1542786069.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=151146938.1.10.1542786069; depovince=SD; _r01_=1; ick_login=40ff382a-8bae-4c2b-b36c-e3556394c886; ch_id=10016; wp_fold=0; XNESSESSIONID=7f7993d18e59; _ga=GA1.2.1892114639.1542786069; _gid=GA1.2.1989475095.1542786723; t=7ba5a5d00e9992e51527857c3e2e68a07; societyguester=7ba5a5d00e9992e51527857c3e2e68a07; id=967687907; xnsid=cabdb06f; jebecookies=6fc33181-d74d-4de0-a41a-6ddd12843329|||||; jebe_key=644126cc-d66d-43e5-b2d6-634c42442acd%7C3912beb733dea106fffe0c33cfa4917d%7C1542787143465%7C1',
    }
    req = request.Request(url=url,headers=headers)
    resp = request.urlopen(req)
    with open("renren.html","w",encoding='utf-8') as fp:
        fp.write(resp.read().decode("utf-8"))