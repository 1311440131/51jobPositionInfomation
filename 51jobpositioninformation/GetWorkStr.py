#coding:utf-8

import re
import urllib2

def getWorkStr(url):
    header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    #url = "https://jobs.51job.com/shanghai/120788731.html?s=01&amp;t=0"
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    pageSource = response.read()

    restr = """ <div class="bmsg job_msg inbox">([\s\S]*?)<div class="mt10">"""
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(pageSource)
    if len(mylist) != 0:
        lastStr = mylist[0].strip().decode('GBK').replace("<p>", "").replace("</p>", "").replace("<b>", "").replace("</b>", "").replace("<div>", "").replace("</div>", "").replace("<span>", "").replace("</span>", "").replace("&nbsp;", "").replace("<br>", "").replace("</u>", "").replace("<u>", "").replace("<ol>", "").replace("<li>", "").replace("</li>", "").replace("</ol>", "").replace("<P>", "").replace("<br />", "").replace("</P>", "")
        return lastStr




