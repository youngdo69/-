from pymongo import MongoClient
# pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.sparta09

bring_movie = db.movies.find_one({'title': '월-E'})
target_star = bring_movie['star']

movies = list(db.movies.find({'star': target_star}))

for movie in movies:
    print(movie['title'])



db.movies.update_many({'star': target_star}, {'$set': {'star':0}})

