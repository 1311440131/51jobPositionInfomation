#coding:utf-8


import GetSingleUrlFromZhaoPin
import GetUrlListFromZhaoPin
import GetWorkStr

# 创建一个保存workStr的文件
fileSavePath = "workStr.txt"
saveFile = open(fileSavePath, "wb")

# 1--首先获取所有页的url
urlList = GetUrlListFromZhaoPin.getUrlListfromName("python")
# 2--从每页中获取每一项的url
for pageUrl in urlList:
    pageHrefs = GetSingleUrlFromZhaoPin.getHrefFromUrl(pageUrl)
    # 从每一项中获取工作str信息
    for href in pageHrefs:
        workStr = GetWorkStr.getWorkStr(href)
        print workStr
        if workStr != None:
            saveFile.write((workStr+"\r\n").encode('utf-8'))

saveFile.close()



