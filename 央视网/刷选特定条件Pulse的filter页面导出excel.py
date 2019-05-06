#-*- coding:utf-8 -*-
import requests
import json
import csv
import time


rule_attrs = ['c3.br','c3.pt.br','c3.client.br','c3.br.v','c3.pt.br.ver','c3.client.brv','c3.device.model','c3.client.model','c3.client.marketingName','c3.device.type','c3.client.hwType','c3.device.ver','c3.client.brand','c3.client.brand','c3.device.manufacturer','c3.client.manufacturer','c3.framework','c3.framework.ver','c3.pt.os','c3.fp.os','c3.client.osf','c3.client.osName','c3.pt.os.ver','c3.client.osv','c3.pt','c3.client.osName','c3.pt.ver,Browser','Browser Version','Device Model','Device Type','Device Version','Flash Version','Framework','Framework Version','OS','OS Version','Platform','Platform Version']
def parserHtml(text):
    aa = text.split("script")
    try:
        bb = aa[-4].split("new pulse.modules.FilterTable(")[1].replace(",true,true,true); });</","")
    except:
        print("Cookie过期了,所以报错")
    cc = str(bb)
    dd = json.loads(cc)
    data =[]
    incluede_data = []
    excluede_data = []
    for d in dd:
        fid = d.get("fid")
        rules = d.get("rules")
        creator = d.get("creator")
        name = d.get("name")
        created = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(d.get("created"))/1000))
        is_advanced = d.get("is_advanced")
        for attr in rule_attrs:
            if "("+attr in rules:
                oo = (fid,creator, name, rules, created, is_advanced)
                incluede_data.append(oo)
                break
            if attr==rule_attrs[len(rule_attrs)-1] and attr not in rules:
                oa = (fid,creator, name, rules, created, is_advanced)
                excluede_data.append(oa)
                break
    print("incluede_data:"+str(incluede_data))
    print("excluede_data"+str(excluede_data))
    return incluede_data, excluede_data


def generate_file(ff,filename):
    csvfile = open(filename, 'w',newline="")
    writer = csv.writer(csvfile)
    writer.writerow(['fid','creator','name', 'rules','created',"is_advanced"])
    for f in ff:
        writer.writerow(f)

    csvfile.close()

if __name__=='__main__':
    url = "https://pulse.conviva.com/filters/"
    # 需要复制浏览器的cookie
    cookie=''
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
        # "Authorization":"Basic "+str(a)
        "Cookie":cookie,
        "Host": "pulse.conviva.com",
        "Pragma": "no-cache"
    }

    # 禁用安全请求警告
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url,headers=headers,verify=False)
    # 禁用安全请求警告
    with open("filters.html",'w',encoding='utf-8') as fp:
        fp.write(res.content.decode('utf-8'))
    incluede_data,excluede_data = parserHtml(res.text)
    generate_file(incluede_data,'include.csv')
    generate_file(excluede_data,'exclude.csv')