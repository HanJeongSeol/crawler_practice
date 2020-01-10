from bs4 import BeautifulSoup

html = """
<html><body id = "main">
    <h1 class = "str"> 스크레이핑이란?</h1>
    <p1>웹 페이지를 추출하는 것</p1>
    <p2>원하는 부분을 추출하는 것</p2>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

# h1 = soup.html.body.h1
# p1 = soup.html.body.p1
# p2 = soup.html.body.p2

h1 = soup.select_one("h1.str")
p1 = soup.select_one("#main > p1")
p2 = soup.select_one("html p2")

print("h1 = " + h1.string)
print("p1 = " + p1.string)
print("p2 = " + p2.string)