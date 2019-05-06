#-*- coding:utf-8 -*-
from lxml import etree

if __name__ == '__main__':
    parser = etree.HTMLParser(encoding='utf-8')
    html = etree.parse('tencent.html',parser=parser)
    # 1.获取所有tr标签
    trs = html.xpath('//tr')
    #xpath函数返回一个列表
    for tr in trs:
        print(tr)
    print('----------------1')
    # 2.获取第二个tr标签
    t = html.xpath('//tr[2]')[0]
    print(etree.tostring(t, encoding='utf-8').decode('utf-8'))
    print('----------------2')
    # 3.获取所有的class等于even的标签
    # trs1 = html.xpath("//tr[@class='even']")
    trs1 = html.xpath("//tr")
    for tr in trs1:
        print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))
    print('----------------3')

        # 4.获取所有的a标签的href属性
    abs = html.xpath('//a[@title]/@href')
    for a in abs:
        print('http://hr.tencent.com/'+a)
    print('----------------4')
#5.获取所有职位信息(纯文本)
    trs2 = html.xpath("//tr[position()>1]")
    for tr in trs2:
        href = tr.xpath('.//a/@href')[0]
        fullurl = 'http://hr.tencent.com/'+href
        title = tr.xpath('//td/a[@title]/text()')[0]
        address = tr.xpath()
        print(title)
        break


