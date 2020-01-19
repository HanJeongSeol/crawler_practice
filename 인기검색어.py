from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse
import requests
import lxml.html

url = "https://www.daum.net/"
url_news = "https://search.naver.com/search.naver?where=news&sm=tab_jum&"
code = req.urlopen(url)
soup = BeautifulSoup(code, "html.parser")
data = soup.select("div.hotissue_builtin ol.list_hotissue.issue_row span.txt_issue")
keyword = ""
for i in range(len(data)):
    if i%2 == 1:
        keyword = data[i].string
        values = {'query' : keyword}
        params = urllib.parse.urlencode(values)
        url_result = url_news + params
        result_news = req.urlopen(url_result)
        soup_news = BeautifulSoup(result_news, "html.parser")
        data_news = soup_news.select("ul.type01 a")
        count = 0
        index = -1
        while count < 3:
            index +=1
            if("title" not in data_news[index].attrs.keys()):
                continue
            print("관련기사:", data_news[index].attrs["title"])
            count += 1
        print()
