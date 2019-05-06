
#-*- coding:utf-8 -*-

import requests
import time
import json

if __name__=='__main__':
    url = "https://drm.live.cntv.cn/udrm/udmCNTVGetLicense"
    # url = "https://pulse.conviva.com/login"
    # url = "https://pulse.conviva.com/login?next=/reports/1"
    # a = base64.b64encode("xiaopeng.wang@trvqd.com:Trvqd@123.com".encode("utf-8"))
    # 需要复制浏览器的cookie
    tt = int(time.time())
    print(tt)
    # cna CVE编号权限
    # vjuids uuid

    # cookie = "_ga=GA1.2.738698131.1536573505; __utmz=231626398.1536574063.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pendo_visitorId.7df8727f-b771-4e46-6ae1-f3c3bb45f266=xiaopeng.wang%40trvqd.com; __utmv=231626398.|1=Customer=c3.CCTV=1; _pendo_accountId.7df8727f-b771-4e46-6ae1-f3c3bb45f266=c3.CCTV; _pendo_meta.7df8727f-b771-4e46-6ae1-f3c3bb45f266=3553514628; _gcl_au=1.1.420519605.1541496871; _gid=GA1.2.1052852850.1541496873; __utma=231626398.738698131.1536573505.1541494788.1541502026.70; __utmc=231626398; __utmt=1; __utmb=231626398.8.10.1541502026; sessionid=97be1fd644d40ad149be06e313bfb3bf"
    cookie = "" \
             "cna=hkUdFIzhezMCAXuoWB6Lf3Ly; " \
             "vjuids=58e2241dd.165d7246860.0.211b43ea07e; " \
             "vjlast=1536912812.1536912812.30; " \
             "_gscu_860483372=36912814chzn0223; " \
             "isg=BF5e5E7eiRKJ4t32Vflc5gRXr_RgtyPzVUAoYgjnyqGcK_4FcK9yqYQqJ3eCExqx"
    headers = {
           "Host":"drm.live.cntv.cn",
            "Connection":"keep-alive",
            "Content-Length":"584",
            "Origin":"http://player.cntv.cn",
            "X-Requested-With":"ShockwaveFlash/31.0.0.122",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded",
            "Accept":"*/*",
            "Referer":"http://player.cntv.cn/standard/live_HLSDRM20181022.swf?v=180.171.5.8.9.6.3.9",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
            # "Cookie":cookie
        }
    # version:版本
    # platform:平台代号
    # cdn:cdn
    #deviceID:设备标识
    #drmServerID：drm服务器的id
    #nonce:随机字符串
    # timestamp:时间戳
    # contentIDs:内容ID
    # certificateChain:不知道是啥，不影响获取drm
    # signature:签名
    # data = {"version":"3.0","platform":"1","cdn":"3","deviceID":"MTAzMDgwMDAwMDAwMDA3MA==","drmServerID":"CNTV","nonce":"1C8VbqiuEulMN4/kfKJwMgMepwg=","timestamp":"1541930400","contentIDs":["MjgyMDE4MDUxNjAwMQ=="],"certificateChain":[],"signature":"VJSlwdjWrq0//IoFLcVztDF8CH032Ko0siuQcjQ5vo0WYAO4hlj5QbACoL2DmjcZwLJP13Mi+3oy20+BDcUFF004RS3vU4/F5RXw2hJOq2/ARow7aNDbOCZXONoiDemeiGaXk4gMamdL4TS4xZNx3KR/RlniiByBXV8GxFBdKOkDyfdwsVgk3vXjcX8PkGTzzgRs1hlmd5NI8S7Q8bUIF9gPPKsu2cBce/R0UPuZJQh8KxGFl5KOuche6d/YMXY3OMkAHZh4OdpBwrF5knO2HlR/44EhqvVgDC52KMvvbGTFGabeRfEDLY1thzgbxBxqtC/++G0j20UUVxtJl2/iIQ=="}
    # data = {"version":"3.0","platform":"1","cdn":"3","deviceID":"MTAzMDgwMDAwMDAwMDA3MA==","drmServerID":"CNTV","nonce":"RPtJzj0SRPKwwQdbyhMAMKu0IF4=","timestamp":"1541930400","contentIDs":["MjgyMDE4MDUxNjAwMQ=="],"certificateChain":[],"signature":"G9myK9sHCcI0DqTb/eBzQyGZgHZPv6t21ojDwxWbaz8C40QWhakfMpW9F4INx/zrK/g9xH4A/DGtgL/X0nMK5Hig3CAdG5EPgNIulTy7yEGBGSMfe6EXegFf0hOLn2va6hPsBn5yMd6TmJnvAyTFJDF/M1yFf7yqljKblWJOHlTr5XsLfrt4R6TKv57ZdbukLyZTR0k6tTowOa6S+0PCl5C7htChgebSlfyvswf9Nk846GDI9RZpXIUb9/sj4q2UaOtEd+oWbf0F54F/12MU3L+lZRdgy473q8+U0elZmjPftqPcVSft5fmaBEG5zwIisnmPkORrex2aPRlUY8EqnQ=="}
    # data = {"version":"3.0","platform":"1","cdn":"3","deviceID":"MTAzMDgwMDAwMDAwMDA3MA==","drmServerID":"CNTV","nonce":"RPtJzj10SRPKwwQdbyhMAMKu0IF4=","timestamp":"1542077139","contentIDs":["MjgyMDE4MDUxNjAwMQ=="],"certificateChain":[],"signature":"TP/KezXs8FGRzumVc65BlVPB4++NWQAYqy/HO/hzw4Ku0f9GKDO7B1FAiSNFTNqABOuGdry9sbsfO5w2AkxOsX+rlqSD/ppr5F1EuW/PcVDiCQh1FsG0ckBmHsNJSteOzrmMiuhNYeksjbiJJMQk6SeYdiIVzh7CnHAm25SsKjcYrPCwq9PnuTLU8YDZC03FajyIdjvrj620iwABvimWF9kwuJ1QjOP/gk5B8+2+GfbGNnZpjfX8QGkvlq4K6HB7/B/9loMLdXOAOWNeOqxIvcexXFXRqbIfaZ8VbPgjhpjf6S7m+yGYdNFiDS4W1QmhXiR4EtRVl48scSZrL1Qktw=="}
    # res = requests.get(url,headers=headers,verify=False,data=data)
        # res = requests.get(url,verify=False)
    data = {"version":"3.0","platform":"1","cdn":"1","deviceID":"MTAzMDgwMDAwMDAwMDA3MA==","drmServerID":"CNTV","nonce":"5lst3Ldell+QECZ9VqIf5yy7Dfw=","timestamp":"1542103440","contentIDs":["MjgyMDE4MDUxNjAwMQ=="],"certificateChain":[],"signature":"7777/NNEIkqrRnA5tu122YLGp4/zL5EjEsPTLZM1Vpi2xI4r5ir1Y9dikzmySxvt5xQ9EqxIDP/84Laab8MVDm6wt1gyxIVl0Sijzxb2WzAnz+0rxx5rlJgZIu1riXS5XvTL0puq1116TestdU+NVVgtteLnnL3/dOSbn/Bp0YuGamsLt5/E6yRCeCsa/i/9lZ6gMgyHwFfPbrDmMgCwfOUJXoUdCdSgT01PXUYqqrOeiLnXvb/qy2wZcAW/lKhURaGURViSRavAhQVWWGLFT8V6IyTumHvIT9MKS1H+mBRphCCL0w=="}
    textmod = json.dumps(data).encode("utf-8")
    from requests.packages.urllib3.exceptions import InsecureRequestWarning

        # 禁用安全请求警告
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    # version:版本号
    # status:状态码
    # nonce:客户端上传的随机数
    # protectedLicenses：私有证书
    # contentId：客户端上传的节目ID
    # licenses：许可（应该可能有多个）
    # licenseID：许可ID
    # license：许可信息
    # certificateChain：证书链
    # {"version": "3.0", "status": 0, "nonce": "111", "protectedLicenses": [{"contentId": "MjgyMDE4MDUxNjAw1MQ==",
    #                                                                        "licenses": [{
    #                                                                                         "licenseID": "YWR4bGJhcm8wMDAwMDAwMDAwMDAwMDAwMDAwMDAzMjk=",
    #                                                                                         "license": "mOaxIWG+8tYjS8YNrFiY49kIJbHA/yaR3PGQRvYSPsHyAib/jwwJj90fd2N1f4D8Q6RC6nPwFSvE\nLt29zfj+dhq2s46lU+M6C2QJXmiQamH69UGnRuTsznKpVvtDy3UKS+GzyRIbhsxUhQY5FcPrTnmx\nNwBd4Y/R2ZpgrJFmpxm9P/o5abnvWVx7sNKdo2pwvwgigF9U9CO20UlksA5uxLj0pcBHrJr4EIlg\nf+qnHqCxCjeCgMRDk8u8AM3xkYHZapV3z/DMGlMyKYDgTvY5RwKxfkUWt57P60GQ6RVRR6LgnjM0\nxfjwjLmx1SdRUdXYmDbqGYzT+wCFDJIfjWS1LPtNv6TiyQgGhwERFUW1zi6hOhT8BQafsg=="}]}],
    #  "certificateChain": [
    #      "MIIEsTCCA5mgAwIBAgIDAYaiMA0GCSqGSIb3DQEBCwUAMGYxCzAJBgNVBAYMAkNOMQswCQYDVQQIDAJCSjELMAkGA1UEBwwCSEQxDDAKBgNVBAoMA0RSTTEQMA4GA1UECwwHdW5pdGVuZDEMMAoGA1UEAwwDdXRpMQ8wDQYDVQQMDAZ2My4wLjAwHhcNMTgwMTE0MDkwNTQyWhcNMjgwMTEzMDkwNTQyWjBmMQswCQYDVQQGDAJDTjELMAkGA1UECAwCQkoxCzAJBgNVBAcMAkhEMQwwCgYDVQQKDANEUk0xEDAOBgNVBAsMB3VuaXRlbmQxDDAKBgNVBAMMA3V0aTEPMA0GA1UEDAwGdjMuMC4wMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvBCY1V+Sj0Xo64SyxJ1x2nRYOUHT2jyNMc1O5ltIwfRoHWmcEz/8hF+4QnWPjpXHuJopylhTT31t+Nosv2pw8lq5gC7oCk75zFX7xSKfN+Cgf/7vM8IPtOvxyYs22/fY7aN9t0EwLPYysi2sPjzeqb+rjkFg+gkolsIZ/o/eqs/qH7lhbxFYQMo2S1ad6+Yj01N6a0OI4X2ByNPh5lYicPSZM64dmwkNJQdM34Bfv8SBcNguiw8Rh9obx1YyteWmc/aFyQrFpMYMIoQKEgKwZFVOcMpPgv5aRTL+zHoAyf2FMVs7FHRzdxB1wY4bMQjbUEokW+Iu3mzCv/Z+BV/71wIDAQABo4IBZjCCAWIwCQYDVR0TBAIwADAsBglghkgBhvhCAQ0EHxYdIkNFUy1DQSBHZW5lcmF0ZSBDZXJ0aWZpY2F0ZSIwHQYDVR0OBBYEFB4qfV4/GxlMCPTd+iE9+4r4UaOCMIGSBgNVHSMEgYowgYeAFAeN6s6qNXINTwEn7pqKZUXS0aHOoWqkaDBmMQswCQYDVQQGDAJDTjELMAkGA1UECAwCQkoxCzAJBgNVBAcMAkhEMQwwCgYDVQQKDANEUk0xEDAOBgNVBAsMB3VuaXRlbmQxDDAKBgNVBAMMA3V0aTEPMA0GA1UEDAwGdjMuMC4wggMBhqAwCwYDVR0PBAQDAgPoMB8GA1UdJQQYMBYGCCsGAQUFBwMCBgorBgEEAYI3CgMBMDQGA1UdHwQtMCswKaAnoCWGI2h0dHA6Ly93d3cudW5pdGVuZDQuY29tL2NybC9jcmwuY3JsMA8GBSoDBAUGBAYWBE5VTEwwDQYJKoZIhvcNAQELBQADggEBAG92MLp1YTSspizhJVEhuRRLXwNoV7lXVs/MIizGy7IkHyLnr3ncscQwwtTfoTaXvxh521o9msM7z9QBwAGOgPlFZGmdbQvKAKbK0fZ8YdgEx6JvBF1R6w1m/YpPKcYnJcwW6Ej8EA6DzYSrn2GDkWdBOV7U44dovKvLAMmylOhK9Xc4ZTp4XR3rW0a8K3qF+qB3EYNFjYB4lydke40t3Oe38C13PojRrxUn7yCsFbs3Akq1fTlDR/r2IKquXJ6vacnwRY8rrtnsss1sPeY8FUKYslanJGv95+cei2Q/+lDQUKktd2Q0bA1+cRXvQ4OfDuXYynysZyZ/8tF9cTIHg1o=",
    #      "MIIEsTCCA5mgAwIBAgIDAYahMA0GCSqGSIb3DQEBCwUAMGYxCzAJBgNVBAYMAkNOMQswCQYDVQQIDAJCSjELMAkGA1UEBwwCSEQxDDAKBgNVBAoMA0RSTTEQMA4GA1UECwwHdW5pdGVuZDEMMAoGA1UEAwwDdXRpMQ8wDQYDVQQMDAZ2My4wLjAwHhcNMTgwMTE0MDgzOTQ0WhcNMjgwMTEzMDgzOTQ0WjBmMQswCQYDVQQGDAJDTjELMAkGA1UECAwCQkoxCzAJBgNVBAcMAkhEMQwwCgYDVQQKDANEUk0xEDAOBgNVBAsMB3VuaXRlbmQxDDAKBgNVBAMMA3V0aTEPMA0GA1UEDAwGdjMuMC4wMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3OIThNVRE9JYhX8OcftGfcE88xI8Sx2fZbWHuBlPDoaiGZ5txIKLY6YT79pNwan00pGhqDjg215HaF3eVVbGEaMVLPJMtu2C7OHwDC1q/shbO8UPKZY4qGk9R8uVy3cOQU4ex22QzeXOXyzZR7P4gY6VyvKKWRX6A0VLf5koD8X1x2pkR+xiIVlOZmaHSY+pwQDgleroYRdI3FxSfurL15r08Mf4J/QI1xru8gGkb4QcwlPSWTG7uqf3hRd+UgSCa5uLBcqIasC+AfAFR9FpWvs2ZDiE75b3cpTHcKm0sqEtgELPdjeG1wvdpDl8DIlkjsiqt6lRMlgSYTyVx11M7wIDAQABo4IBZjCCAWIwCQYDVR0TBAIwADAsBglghkgBhvhCAQ0EHxYdIkNFUy1DQSBHZW5lcmF0ZSBDZXJ0aWZpY2F0ZSIwHQYDVR0OBBYEFKWZUzDOzlVFgxRMVzRjeHD6TIntMIGSBgNVHSMEgYowgYeAFAeN6s6qNXINTwEn7pqKZUXS0aHOoWqkaDBmMQswCQYDVQQGDAJDTjELMAkGA1UECAwCQkoxCzAJBgNVBAcMAkhEMQwwCgYDVQQKDANEUk0xEDAOBgNVBAsMB3VuaXRlbmQxDDAKBgNVBAMMA3V0aTEPMA0GA1UEDAwGdjMuMC4wggMBhqAwCwYDVR0PBAQDAgPoMB8GA1UdJQQYMBYGCCsGAQUFBwMCBgorBgEEAYI3CgMBMDQGA1UdHwQtMCswKaAnoCWGI2h0dHA6Ly93d3cudW5pdGVuZDQuY29tL2NybC9jcmwuY3JsMA8GBSoDBAUGBAYWBE5VTEwwDQYJKoZIhvcNAQELBQADggEBABo1i10zfMfj9z1kMFtySqx/ZoPxPJgoDg9QxbwjmhRMsEzfV8/LUrvOLPUud7jJZHaFjeV4o+XFi+6oWj6FIpjd+vjsVXDS5/FzsrnP/H7XsNmJQ21EsWFQlqqfk9q/PgGlD0iJDmFBjhWkFX4D98598Sz59rv6BTAMEjoPNGZLKEsyWUc344XBPyxY/eq6vZNJFKCqRNTOpN9BkPZzSBYAXTNK3H25tD4Kw5HD+ovM/9QQGwDzgFM7GUheZxvcfBE9QlXTlI08Mj/3zbs6OCpVEVXum00Yzhesbcwze1zcfPhfzOerCudhHBsQe2LPTmjG2aDL+Ebe/Y7oXIaCraA=\t",
    #      "MIIEvTCCA6WgAwIBAgIDAYagMA0GCSqGSIb3DQEBCwUAMGYxCzAJBgNVBAYMAkNOMQswCQYDVQQIDAJCSjELMAkGA1UEBwwCSEQxDDAKBgNVBAoMA0RSTTEQMA4GA1UECwwHdW5pdGVuZDEMMAoGA1UEAwwDdXRpMQ8wDQYDVQQMDAZ2My4wLjAwHhcNMTgwMTE0MDgyMzI5WhcNMjgwMTEzMDgyMzI5WjBmMQswCQYDVQQGDAJDTjELMAkGA1UECAwCQkoxCzAJBgNVBAcMAkhEMQwwCgYDVQQKDANEUk0xEDAOBgNVBAsMB3VuaXRlbmQxDDAKBgNVBAMMA3V0aTEPMA0GA1UEDAwGdjMuMC4wMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtbt3oOhYVaJpMrfP5XZZaUXHcL6w1TTPc1TFESW8vAKbo4TYGObA7NjZshFWV7vnyQWlzahCMPPnNuGxwUa9RcSM2tBH20mksy4J5uzcpep6A735vF5pga/xHdVqlmPyPyCdp1ZL6vLR1cC/22lPKkcj2b5pgcmR2F4tF3mW+VQaKA0RErRiW/zQ3b/G9INk/glaHwn1J5oLzYFzUFE2JTXIkH2xlpTkkff4lZXqDtYgp2yLDCRfclmtmYeEuILstHUZQxm6+XgoM+q71NWiZIKB6FLZRu7bMPzYJakvn89zlxo3LXM0Wz02NvFPP4ikfDJbVjxe09XNdHhMiISyyQIDAQABo4IBcjCCAW4wCQYDVR0TBAIwADAsBglghkgBhvhCAQ0EHxYdIkNFUy1DQSBHZW5lcmF0ZSBDZXJ0aWZpY2F0ZSIwHQYDVR0OBBYEFAeN6s6qNXINTwEn7pqKZUXS0aHOMIGSBgNVHSMEgYowgYeAFAeN6s6qNXINTwEn7pqKZUXS0aHOoWqkaDBmMQswCQYDVQQGDAJDTjELMAkGA1UECAwCQkoxCzAJBgNVBAcMAkhEMQwwCgYDVQQKDANEUk0xEDAOBgNVBAsMB3VuaXRlbmQxDDAKBgNVBAMMA3V0aTEPMA0GA1UEDAwGdjMuMC4wggMBhqAwCwYDVR0PBAQDAgPoMB8GA1UdJQQYMBYGCCsGAQUFBwMCBgorBgEEAYI3CgMBMDQGA1UdHwQtMCswKaAnoCWGI2h0dHA6Ly93d3cudW5pdGVuZDQuY29tL2NybC9jcmwuY3JsMBsGBSoDBAUGBBIWEDgwNzU1ODgwMDAwMTExMTEwDQYJKoZIhvcNAQELBQADggEBALQyKudHfeSFl8azd1hZzO1n6P+XVXa/LQ+FYiMLDYsm70vMZJDNDrzbOomWhh2ol1clymp/de3RSZ18omu4DGZUAiBxVKrinaM0JR4y4Ej2q+nlk5/B/fqyw9MRAqAHCCEhxPrha4Z3JiJdIJ5fiU6gBs1EVcvhQ/HD6xZ7tKmTZksPU2/u1Nxvwvq+Dn2JMDUaaYWtFc2aDkHCLeUpEG5q1yI/uTQMBsHVISlZsaq3ulfVF43WZkbKiQAvQIUTTOM7SwVqQQNYVMRYADuW/py/cYUe6V5lvxgjtO2KtnxNAgbq8Df0WOA1Mic54Qq71jS7bxeCq1vvSOwm2NmmqcA=\t"],
    #  "ocspResponse": [""], "signature": ""}

    res = requests.post(url,data=json.dumps(data),headers=headers,verify=False)

    print(res.text)
