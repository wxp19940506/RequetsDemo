#-*- coding:utf-8 -*-
import requests
import csv
import re

def generate_file(ff):
    csvfile = open('users.csv', 'w',newline="",encoding='utf-8')
    writer = csv.writer(csvfile)
    writer.writerow(['Username','First name', 'Last name','Email','Role','Last access'])
    # writer.writerow(ff[0])
    for f in ff:
        writer.writerow(f)

    csvfile.close()

if __name__=='__main__':
    url = "https://pulse.conviva.com/users/"
    # 需要复制浏览器的cookie
    cookie = '_ga=GA1.2.968330255.1552443444; __utmz=231626398.1552443938.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pendo_visitorId.7df8727f-b771-4e46-6ae1-f3c3bb45f266=xiaopeng.wang%40trvqd.com; __utmv=231626398.|1=Customer=c3.CCTV=1; _pendo_accountId.7df8727f-b771-4e46-6ae1-f3c3bb45f266=c3.CCTV; _pulse_session_id=0ea78fc2a1aefb548908ef3dd2a0ae37; sessionid=0ea78fc2a1aefb548908ef3dd2a0ae37; _pendo_meta.7df8727f-b771-4e46-6ae1-f3c3bb45f266=2757797822; __utma=231626398.968330255.1552443444.1554687042.1554703811.40; __utmc=231626398; __utmt=1; __utmb=231626398.2.10.1554703811'
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
    print(res.content)
    # 禁用安全请求警告

    pattern = r'<table .*</table>'
    result = re.findall(pattern,str(res.content,encoding='utf-8'))
    print(result[0])

    from lxml import etree
    page = etree.HTML(result[0].encode('utf-8'))
    trs = page.xpath('//tr')
    data = []
    for d in trs:
        # print(d)
        Username,FirstName,LastName,Email,Role,LastAccess  = d.xpath('./td/div/@title')
        # if Username =='xinpeng.li@trvqd.com':
        #     print(etree.tostring(d, encoding='utf-8').decode('utf-8'))

        oo = (Username,FirstName,LastName,Email,Role,LastAccess)
        data.append(oo)

    generate_file(data)
    # print(str(data))


def generate_file(ff):
    csvfile = open('users.csv', 'w',newline="")
    writer = csv.writer(csvfile)
    writer.writerow(['Username','FirstName', 'LastName','Email','Role','LastAccess'])
    # writer.writerow(ff[0])
    for f in ff:
        writer.writerow(f)
    csvfile.close()

