import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient# pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.sparta09    # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for tr in trs:
    rank = tr.select_one('td.number').text[0:2].strip()
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    singer = tr.select_one('td.info > a.artist.ellipsis').text

    genie_doc = {                                    # db 에 들어갈 서류양식을 dictionary 형태로 만들어줌
         'rank':rank, 'title':title, 'singer':singer
    }

    db.genie.insert_one(genie_doc) # genie 라는 콜렉션을 db에 만들고 여기에 앞서 만든 genie_doc 양식의 데이터를 넣어줌 (아직 for문 안에 있는 상태임)


