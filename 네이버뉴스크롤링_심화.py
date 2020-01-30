'''
    네이버 뉴스의 IT분야 기사 title과 본문 내용 수집
'''

from bs4 import BeautifulSoup
import urllib.request as req

url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
code = req.urlopen(url)
soup = BeautifulSoup(code, "html.parser")
results = soup.select("div#main_content a")
output_total = ""
for i in range(len(results)):
    if results[i].string == None:
        continue
    if str.strip(results[i].string) == "헤드라인 더보기":
        break
    print("기사 제목 : {}".format(results[i].string))
    news_url = results[i].attrs['href']
    print("기사 링크 : {}".format(news_url))
    news_code = req.urlopen(news_url)
    news_soup = BeautifulSoup(news_code, "html.parser")
    news_results = news_soup.select_one("div#articleBodyContents")
    for j in news_results.contents:
        # news_results.contents의 type은 list이다. 원하는 text만 출력하기 위해서는 string형태로 변환해야한다.
        # 따라서 str(j)로 string type으로 변경한 후에 strip()을 사용하여 공백을 제거해준다.
        i = str(j).strip()
        # 불필요한 공백 출력 x
        if i == "":
            continue
        if "본문 내용" in i:
            continue
        if "TV플레이어" in i:
            continue
        if "기자" in i:
            continue
        if "<" in i or "[" in i or "]" in i:
            continue
        if "article_split" in i:
            continue
        if "@" in i or "ⓒ" in i or "▶" in i:
            break
        # print(i)
        output_total += j
    print()

print(output_total)
# from konlpy.tag import Twitter, Okt
# from konlpy import init_jvm
# from collections import Counter
#
# # init_jvm("<JAVA_HOME>")
# # spliter = Twitter()
# spliter = Okt()
# print(spliter.nouns(output_total))
# nouns = spliter.nouns(output_total)
#
# count = Counter(nouns)
#
# import numpy as np
# from PIL import Image
#
# korea_coloring = np.array(Image.open("earth.png"))
#
# from wordcloud import ImageColorGenerator
#
# image_colors = ImageColorGenerator(korea_coloring)
#
# from wordcloud import WordCloud
#
# wordcloud = WordCloud(font_path="Daum_Regular.ttf", \
#                       mask=korea_coloring, \
#                       background_color='white').generate_from_frequencies(count)
#
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(10, 10))
# plt.imshow(wordcloud.recolor(color_func=image_colors))
# plt.axis('off')
# plt.savefig('wordcloud.jpg')
# plt.show()
