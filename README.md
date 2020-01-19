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