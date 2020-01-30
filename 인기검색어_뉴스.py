'''
    data_news의 태그를 넓게 잡아서 기사 하나의 title과 하위로 연관된 기사 2가지의 title를 출력하도록 한다.
'''
# from bs4 import BeautifulSoup
# import urllib.request as req
# import urllib.parse
#
# url = "https://www.daum.net/"
# code = req.urlopen(url)
# soup = BeautifulSoup(code, "html.parser")
# data = soup.select("div.hotissue_builtin.hide div.roll_txt span.txt_issue > a.link_issue")
# for i in range(len(data)):
#     if i % 2 == 1:
#         values = {'query': data[i].string}
#         params = urllib.parse.urlencode(values)
#         url_news = "https://search.naver.com/search.naver?where=news&sm=tab_jum&{}".format(params)
#         code_news = req.urlopen(url_news)
#         soup_news = BeautifulSoup(code_news, "html.parser")
#         data_news = soup_news.select("ul.type01 a")
#         count = 0
#         '''
#             뉴스 페이지에서 select("ul.type01 a")로 데이터를 찾으면 title이 존재하지 않는 태그도 포함된다.
#             따라서 title 속성이 존재하지 않으면 index를 증가시켜 다음 태그를 검색한다. --> continue사용
#             title 속성이 존재할 때 해당 부분의 title를 출력하며, count를 증가시켜 3개의 기사만 보이게 한다.
#         '''
#         index = -1
#         while count < 3:
#             index += 1
#             if "title" not in data_news[index].attrs.keys():
#                 continue
#             print("관련기사:{}".format(data_news[index].attrs['title']))
#             count += 1
#         print()


from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse

url = "https://www.daum.net/"
code = req.urlopen(url)
soup = BeautifulSoup(code, "html.parser")
data = soup.select("div.hotissue_builtin.hide div.roll_txt span.txt_issue > a.link_issue")
for i in range(len(data)):
    if i % 2 == 1:
        values = {'query': data[i].string}
        params = urllib.parse.urlencode(values)
        url_news = "https://search.naver.com/search.naver?where=news&sm=tab_jum&{}".format(params)
        code_news = req.urlopen(url_news)
        soup_news = BeautifulSoup(code_news, "html.parser")
        data_news = soup_news.select("ul.type01 dl dt a")
        count = 0
        '''
            상위 코드와는 다르게 soup_news.select의 태그 범위를 상세하게 상위 기사 태그만 검색하도록하였다.
            따라서 하나의 기사 title과 연관된 2개의 기사가 아닌 3가지의 독립된 기사를 출력한다.
            이 때에는 index변수 필요없이 data_news[count]로 출력해도 out of range 발생 없이 출력할 수 있다. --> 한 페이지에 최소 10개의 기사가 보여진다.
        '''
        while count < 3:
            print("관련기사:{}".format(data_news[count].attrs['title']))
            count += 1
        print()

