'''
    알라딘 중고서점 사이트에서 검색하고싶은 특정 단어 입력 후 해당되는 책들의 서명과 가격을 출력함.
    문제점 : 새 책, eBook, 중고서적 가격 등 가격이 부분이 여러개로 세분화 되어있음.
    우리는 중고서적 가격을 가져와야하지만 중간에 다른 가격도 불러오기 때문에 어느 순간부터 데이터가 맞지 않음.
    해결해보려했지만 태그에 class명이나 id명이 붙어있지 않아서 어려움.
    -> 알라딘에서 제공하는 API가 존재한다고하니 찿아서 사용해보기.
'''
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse

num = 0
name = input("서명 입력 : ")
value = {'KeyWord' : name}
params = urllib.parse.urlencode(value, encoding='euc-kr')       # 알라딘 페이지의 인코딩 형식 : euc-kr
print(params)
while True:
    num += 1
    url = "https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&{}&page={}".format(params, num)
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")

    book_name = soup.select("a.bo3 > b")
    book_price = soup.select("a.bo_used > b")
    # print(len(book_name))       # len(book_name)은 해당 페이지에서 select()로 탐색한 태그의 갯수, 따라서 페이지의 끝에서는 0이 출력된다
    for i in range(len(book_name)):
        print("======================")
        print("서명 : {}, 가격 : {}".format(book_name[i].string, book_price[i].string))
        # print("len(book_name):{} ".format(i))
    if len(book_name) == 0:     # 종료를 하기위한 if문이 for문 안에 포함되지 않도록 조심.
        print("====================")
        print("크롤링 종료")
        break

'''
    중고 서적 가격이 존재할 때 태그 속성 데이터에 특정 단어가 반복적으로 들어가는 것을 확인.
    해당 데이터를 불러와 데이터 포함 여부를 검사하여 출력해보려했으나 일부 데이터는 무시하고 출력하는 경우 발생.
'''
# from bs4 import BeautifulSoup
# import urllib.request as req
#
# num = 0
# while True:
#     num += 1
#     url = "https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&KeyWord=%C6%C4%C0%CC%BD%E3&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%C6%C4%C0%CC%BD%E3&KeyLastWord=%C6%C4%C0%CC%BD%E3&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&ViewRowCount=25&page={}".format(num)
#     code = req.urlopen(url)
#     soup = BeautifulSoup(code, "html.parser")
#     book_name = soup.select("a.bo3 > b")
#     book_price = soup.select("a.bo_used > b")
#     book_price_check = soup.select("a.bo_used")
#     book_check = soup.select("a.bo_used > span.bo_used_s")
#     text = "&TabType=1"
#     for i in range(len(book_name)):
#         print(book_check[i].string)
#         if text in book_price_check[i].attrs['href']:
#             print(book_name[i])
#         if text in book_price_check[i].attrs['href'] and book_check[i].string != 0:
#             print("=====================================================")
#             print("서명 : {}, 가격 : {}".format(book_name[i].string, book_price[i].string))
#     if len(book_name) == 0 :
#         print("크롤링 종료")
#         break
#

