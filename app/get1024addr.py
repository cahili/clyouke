# -*- coding: utf-8 -*-
# @Author: huerke
# @Date:   2016-09-03 10:43:51
# @Last Modified by:   Administrator
# @Last Modified time: 2016-09-06 18:40:58

# import requests
# import re
# import sys
# import time
# reload(sys)
# sys.setdefaultencoding('utf-8')


# def get_addr():
#     url = "http://get.xunfs.com/app/listapp.php"  # 地址发布url
#     if not testUrl(url):
#         print "[-] Error: 地址发布url:%s访问失败" % url
#         return
#     payload = {'a': 'get', 'system': 'android', 'v': '1.4'}
#     r = requests.post(url, data=payload, timeout=3)
#     if r:
#         content = r.text
#         pattern = re.compile(r"<a (.*?)>(.+?)</a>")
#         result = pattern.findall(content)
#         if result:
#             for u in result:
#                 addr = "http://{}/" .format(u[1])
#                 if testUrl(addr):
#                     return addr
#                     break


# def testUrl(url):
#     try:
#         a = True
#         for i in range(50):
#             time.sleep(1)
#             r = requests.get(url, timeout=3)
#             if r.status_code == 200:
#                 a = a and True
#                 return a
#     except Exception, e:
#         return

caoliuaddr = 'http://cl.dicool.pw/'


# if __name__ == '__main__':
#     try:
#         main()
#     except Exception, e:
#         print "[-] Error: %s" % e
