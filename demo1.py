#-*- coding:utf-8 -*-
# coding: utf-8

import csv

csvfile = open('csv.csv', 'w',newline="")  #打开方式还可以使用file对象
writer = csv.writer(csvfile)
writer.writerow(['姓名', '年龄', '电话'])

data = [('小芳', '18', '789456'),('小1', '18', '789456'),('小w', '18', '789456')]
writer.writerows(data)

csvfile.close()