#-*- coding:utf-8 -*-
import requests
import json


if __name__=='__main__':
    url = "http://tv.cctv.com/live/"
    # data = {"version":"3.0","platform":"1","cdn":"1","deviceID":"MTAzMDgwMDAwMDAwMDA3MA==","drmServerID":"CNTV","nonce":"5lst3Ldell+QECZ9VqIf5yy7Dfw=","timestamp":"1542103440","contentIDs":["MjgyMDE4MDUxNjAwMQ=="],"certificateChain":[],"signature":"7777/NNEIkqrRnA5tu122YLGp4/zL5EjEsPTLZM1Vpi2xI4r5ir1Y9dikzmySxvt5xQ9EqxIDP/84Laab8MVDm6wt1gyxIVl0Sijzxb2WzAnz+0rxx5rlJgZIu1riXS5XvTL0puq1116TestdU+NVVgtteLnnL3/dOSbn/Bp0YuGamsLt5/E6yRCeCsa/i/9lZ6gMgyHwFfPbrDmMgCwfOUJXoUdCdSgT01PXUYqqrOeiLnXvb/qy2wZcAW/lKhURaGURViSRavAhQVWWGLFT8V6IyTumHvIT9MKS1H+mBRphCCL0w=="}
    # textmod = json.dumps(data).encode("utf-8")
    from requests.packages.urllib3.exceptions import InsecureRequestWarning

        # 禁用安全请求警告
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


    res = requests.post(url,verify=False)

    print(res.text)
