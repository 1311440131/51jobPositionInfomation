#coding:utf-8

import urllib
import urllib2
import cookielib
import re
import selenium
import selenium.webdriver

def getHrefFromUrl(url):

    returnUrlList = []

    # 创建一个Edge的浏览器
    driver = selenium.webdriver.Edge()
    #header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    #request = urllib2.Request(url, headers=header)
    # 使用创建的浏览器打开一个Url
    driver.get(url)
    #response = urllib2.urlopen(request)
    # 获得网页源码
    #pagesource = response.read()
    pagesource = driver.page_source
    # 正则表达式，1--提取表格
    restr1 = """<div class="el">([\s\S]*?)</div>"""
    regex1 = re.compile(restr1, re.IGNORECASE)
    tableList = regex1.findall(pagesource)

    #print tableList[0]


    # 正则表达式，2--提取出href消息
    for line in tableList:
        restr3 = """href=\"([\s\S]*?)\" target=\"_blank\">"""
        regex3 = re.compile(restr3, re.IGNORECASE)
        hrefList = regex3.findall(line)
        if len(hrefList) != 0:
            print hrefList[0]
            returnUrlList.append(hrefList[0])
    driver.close()
    return returnUrlList

"""
u = "https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,134.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
print getHrefFromUrl(u)
"""


