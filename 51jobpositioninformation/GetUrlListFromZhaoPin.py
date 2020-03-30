
#coding:utf-8

import urllib
import urllib2
import cookielib
import re
import selenium
import selenium.webdriver

# 如果正则表达式抓取不到数据，一般都是空白的原因
def searchnumbyname(name):
    url = "https://search.51job.com/list/020000,000000,0000,00,9,99,"+name+",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    #driver = selenium.webdriver.Edge()
    #driver.get(url)     # 访问连接
    #pageSource = driver.page_source
    header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    pageSource = response.read()
    #print pageSource
    restr = """ <div class="rt">([\s\S]*?)</div>"""
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(pageSource)
    if len(mylist)==0:
        return "失败"
    else:
        #print mylist[0]
        newstr = mylist[0].strip()  # 前后空格空白符
        #driver.close()
        return newstr


# namelist = ["java", "python", "C++"]

'''
for name in namelist:
    print name
    print searchnumbyname(name)
'''
#print searchnumbyname("python")

def getUrlListfromName(name="python"):
    numstr = searchnumbyname(name)
    numregexstr = "(\\d+)"
    numregex = re.compile(numregexstr, re.IGNORECASE)
    numlist = numregex.findall(numstr)
    #print numlist[0]

    num = eval(numlist[0])

    if  num % 50 ==0:
        pages = num//50
    else:
        pages = num//50+1


    urllist = ["https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,"+str(i) for i in range(1, pages+1)]

    for i in range(len(urllist)):
        urllist[i] += ".html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="

    for line in urllist:
        print line
    return urllist

#getUrlListfromName()