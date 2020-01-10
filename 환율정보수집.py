from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser", from_encoding="ANSI")

# 찾은 데이터의 최상위 요소만 저장, .stirng으로 태그 제거해서 저장
# price = soup.select_one("ul.data_lst span.value").string

# select_one로 찾은 요소 출력
# print(price)

# 국가
nation = soup.select("h3.h_lst span.blind")

# 태그에 해당하는 데이터를 모두 리스트 형태로 저장. 출력할 때 .string 메서드 필요
price_mul = soup.select("ul.data_lst span.value")

# 시장지표 페이지 상단 환전 고시 환율에 해당하는 네 가지 data 추출하기 위한 slice
nation = nation[0:4]
price_mul = price_mul[0:4]

a = {name : value for name, value in zip(nation, price_mul)}

for key, value in a.items():
    print(key.string, " : " , value.string + "원")


# select()로 찾아서 리스트에 저장된 요소드를 모두 출력
# for data in range(len(price_mul) // 3):
#     print(price_mul[data].string)
#
# for nation_name in range(len(nation) // 3):
#     print(nation[nation_name].string)

# dictionary형으로 데이터 저장 후 출력
# dict() : 키-값 연결 , 리스트&튜플&딕셔너리로 딕셔너리 생성
# data_dict = dict