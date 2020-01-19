# 스크레이핑 

### 스크레이핑_test
0. BeautifulSoup 설치 
    1. `pip install beautifulSoup4`
1. BeautifulSoup 모듈 사용법
    1. select()
    

### 환율정보수집
1. 네이버 금융 시장지표 페이지의 상위 환전 고시 환율 4개 국가의 환율 정보 수집
2. b = {name : value for name, value in zip(nation, price_mul)}
    1. for문을 사용하여 dictionary 자료형 생성, zip으로 두 개의 리스트를 하나의 튜플형으로 생성
    2. key값은 name, value값은 value로 저장.
    
### 인기검색어
1. 네이버의 인기검색어 1-10 순위까지 가져와서 해당 키워드의 뉴스 타이틀 3개를 출력하게한다.
    - 네이버 html구조 변경으로 인해서 다음의 인기검색어 키워드로 네이버 뉴스 검색
    - 다음 뉴스 구조는 javascript으로 받아온다.
