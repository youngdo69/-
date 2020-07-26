
import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

green_book_tag = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
print(green_book_tag.text)

movies = soup.select('#old_content > table > tbody > tr')
#:nth-child(2) > td.title > div > a

for movie in movies:
    movie_tag= movie.select_one('td.title > div > a')
    rank_tag = movie.select_one('td:nth-child(1) > img')
    score_tag = movie.select_one('td.point')
    if movie_tag is not None:
        print(rank_tag['alt'],movie_tag.text, score_tag.text)

'''
print(movie_info)
print('title속성', movie_info['title'])
print(movie_info.text)
'''


#############################
# (입맛에 맞게 코딩)
#############################
