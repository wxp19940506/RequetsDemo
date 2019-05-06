#-*- coding:utf-8 -*-
import pywifi
import time
from pywifi import const

# # 判断是否有无线网卡
def gic():
    wifi = pywifi.PyWiFi()#创建一个无线对象
    ifaces = wifi.interfaces()[0]#取第一个无限网卡
    print(ifaces)
    if ifaces in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE] :
        print("已连接")
    else:
        print("未连接")


# 扫描附近的wifi
def bies():
  wifi=pywifi.PyWiFi()#创建一个无限对象
  ifaces=wifi.interfaces()[0]#取一个无限网卡
  ifaces.scan()#扫描
  bessis=ifaces.scan_results()
  for data in bessis:
    print(data.ssid)#输出wifi名称
  return bessis

# 尝试并连接wifi
def deswifi():
    wifi = pywifi.PyWiFi()  # 创建一个wifi对象
    ifaces = wifi.interfaces()[0]  # 取第一个无限网卡
    print(ifaces.name())  # 输出无线网卡名称
    ifaces.disconnect()  # 断开网卡连接
    time.sleep(3)  # 缓冲3秒
    profile = pywifi.Profile()  # 配置文件
    for ssid in bies():
        profile.ssid = "502"  # wifi名称
        # profile.auth = const.AUTH_ASG_OPEN  # 需要密码
        # profile.akm.append(const.AKM_TYPE_WPA2SK)  # 加密类型
        profile.auth = const.AUTH_ALG_OPEN  # 需要密码
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 加密类型
        profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
        ifaces.remove_all_network_profiles()  # 删除其他配置文件
        tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件
        ifaces.connect(tmp_profile)  # 连接
        time.sleep(10)  # 尝试10秒能否成功连接
        isok = True
        if ifaces.status() == const.IFACE_CONNECTED:
            print("成功连接")
        else:
            print("失败")
        ifaces.disconnect()  # 断开连接
        time.sleep(1)
    return isok


if __name__ == "__main__":
    # gic()
    # bies()
    deswifi()