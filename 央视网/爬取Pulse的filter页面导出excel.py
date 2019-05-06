#-*- coding:utf-8 -*-
import requests
import json
import csv
import time

def parserHtml(text):
    aa = text.split("script")
    try:
        bb = aa[-4].split("new pulse.modules.FilterTable(")[1].replace(",true,true,true); });</","")
    except:
        print("Cookie过期了，所以报错")
    cc = str(bb)
    print(cc)
    dd = json.loads(cc)
    data = []
    for d in dd:
        print("d="+str(d))
        fid = d.get("fid")
        creator = d.get("creator")
        rules = d.get("rules")
        name = d.get("name")
        is_advanced = d.get("is_advanced")
        # created = d.get("created")
        created = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(d.get("created"))/1000))
        oo = (fid,creator,name,rules,created,is_advanced)
        data.append(oo)
    return data


def generate_file(ff):
    csvfile = open('filters.csv', 'w',newline="")
    writer = csv.writer(csvfile)
    writer.writerow(['fid','creator','name', 'rules','created',"is_advanced"])
    # writer.writerow(ff[0])
    for f in ff:
        writer.writerow(f)

    csvfile.close()

if __name__=='__main__':
    url = "https://pulse.conviva.com/filters/"
    # url = "https://pulse.conviva.com/login"
    # url = "https://pulse.conviva.com/login?next=/reports/1"
    # a = base64.b64encode("xiaopeng.wang@trvqd.com:Trvqd@123.com".encode("utf-8"))
    # 需要复制浏览器的cookie
    cookie='_ga=GA1.2.968330255.1552443444; __utmz=231626398.1552443938.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pendo_visitorId.7df8727f-b771-4e46-6ae1-f3c3bb45f266=xiaopeng.wang%40trvqd.com; _pulse_session_id=17c8576c80874f65f1ae84113a1656df; sessionid=17c8576c80874f65f1ae84113a1656df; __utmv=231626398.|1=Customer=c3.CCTV=1; _pendo_accountId.7df8727f-b771-4e46-6ae1-f3c3bb45f266=c3.CCTV; __utmc=231626398; _pendo_meta.7df8727f-b771-4e46-6ae1-f3c3bb45f266=4094303288; __utma=231626398.968330255.1552443444.1557118930.1557131199.75; __utmt=1; __utmb=231626398.3.10.1557131199'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
        # "Authorization":"Basic "+str(a)
        "Cookie":cookie,
        "Host": "pulse.conviva.com",
        "Pragma": "no-cache"
    }

    # data = {
    #     "username":"xiaopeng.wang%40trvqd.com",
    #     "password":"Trvqd%40123",
    #     "next":"%2Freports%2F1"
    # }
    # 禁用安全请求警告
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url,headers=headers,verify=False)
    print(res.content)
    # 禁用安全请求警告
    with open("filters.html",'w',encoding='utf-8') as fp:
        fp.write(res.content.decode('utf-8'))
    ff = parserHtml(res.text);
    generate_file(ff)