from pymongo import MongoClient
# pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.sparta09  # 'dbsparta'라는 이름의 db를 만듭니다.



all_user = list(db.users.find({}))


forties = list(db.users.find({'age':40}, {'_id':False}))
for user in forties:
    print(user)

db.users.update_one({'name':'덤블도어'}, {'$set': {'age':19}})
dumble = db.users.find_one({'name': '덤블도어'})
print(dumble)

db.users.delete_one({'name':'론'})
user = db.users.find_one({'name':'론'})
print(user)

