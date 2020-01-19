'''
select_one() : 데이터의 최상위 요소만 저장
select() : 일치하는 데이터 전체를 리스트형으로 저장
-> 찾으려는 데이터의 태그 class, id를 잘못 설정하여 불필요한 작업 추가
    -> price_mul과 nation이 저장되어있는 태그의 css 선택자를 잘못 선택하여 불필요한 데이터까지 들어와버림
    -> 따라서 상위 네 개의 데이터만 출력하기 위해 // 연산자를 사용하여 3으로 나눈 몫까지만 출력
'''

# from bs4 import BeautifulSoup
# import urllib.request as req
#
# url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
# res = req.urlopen(url)
#
# soup = BeautifulSoup(res, "html.parser", from_encoding="ANSI")
#
# # 찾은 데이터의 최상위 요소만 저장, .stirng으로 태그 제거해서 저장
# price = soup.select_one("ul.data_lst span.value").string
#
# # select_one로 찾은 요소 출력
# print(price)
#
# # 국가
# nation = soup.select("h3.h_lst span.blind")
#
# # 태그에 해당하는 데이터를 모두 리스트 형태로 저장. 출력할 때 .string 메서드 필요
# price_mul = soup.select("ul.data_lst span.value")
#
# # select()로 찾아서 리스트에 저장된 요소드를 모두 출력
# for data in range(len(price_mul) // 3):
#     print(price_mul[data].string)
#
# for nation_name in range(len(nation) // 3):
#     print(nation[nation_name].string)

'''
    환전 고시 환율 데이터의 국가, 환율 정보를 하나의 dictionary에 저장시켜 출력한다.
    css 선택자의 범위를 제대로 하지 않아서 불필요한 자료까지 출력되는 코드.
    선택자를 사용하여 불러올 때는 정확한 태그 범위 설정 필요하다.
    정확한 태그범위를 사용했다면 58-59 과정이 불필요하다.
'''

# from bs4 import BeautifulSoup
# import urllib.request as req
#
# url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
# res = req.urlopen(url)
#
# soup = BeautifulSoup(res, "html.parser", from_encoding="ANSI")
#
# # 국가
# nation = soup.select("h3.h_lst span.blind")
#
# # 태그에 해당하는 데이터를 모두 리스트 형태로 저장. 출력할 때 .string 메서드 필요
# price_mul = soup.select("ul.data_lst span.value")
#
# # 시장지표 페이지 상단 환전 고시 환율에 해당하는 네 가지 data 추출하기 위한 slice
# nation = nation[0:4]
# price_mul = price_mul[0:4]
#
# # zip() : 요소들을 순서대로 튜플로 묶는다.
# # dict() : 요소들의 앞에 있는 값을 key, 뒤에 있는 값을 value로 하여 dictionary형 생성
# a = dict(zip(nation, price_mul))
#
# # for문을 사용하여 zip()으로 데이터를 묶는 동시에 dictionary형 생성
# b = {name : value for name, value in zip(nation, price_mul)}
#
# for key, value in b.items():
#     print(key.string, " : " , value.string + "원")


'''
    css 선택자를 수정하여 리스트의 slice가 필요 없이 바로 원하는 값만 출력한다.
    결과는 위 코드와 똑같이 출력되지만 코드의 가독성을 위하여 아래와 같이 수정한다.
'''

from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser", from_encoding="ANSI")

nation = soup.select("ul#exchangeList h3.h_lst span.blind")
price = soup.select("ul#exchangeList span.value")
for data in range(len(nation)):
    print("{} : {}원".format(nation[data].string, price[data].string))
