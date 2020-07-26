fruits_basket = ['사과', '배', '귤', '복숭아', '오렌지', '수박', '포도', '파인애플', '파인애플', '파인애플', '배', '사과']

def count_fruits(fruit_name):
    count = 0
    for fruit in fruits_basket:
        if fruit == fruit_name:
            count += 1
    return count



print('사과', count_fruits('사과'))




professor_wizards = [
    {'name': '덤블도어', 'age': 116},
    {'name': '맥고나걸', 'age': 85},
    {'name': '스네이프', 'age': 60},
]

for wizard in professor_wizards:
    print(wizard['name'], wizard['age'])

def get_age(name, wizards):
    for wizard in wizards:
        if wizard['name']== name:
            return wizard['age']
    return '해당 이름이 없습니다.'

print (get_age('덤블도어', professor_wizards))
print (get_age('맥고나걸', professor_wizards))
print (get_age('스네이프', professor_wizards))
print (get_age('해리포터', professor_wizards))












