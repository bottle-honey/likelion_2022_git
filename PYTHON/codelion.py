import random
import time
lunch = []

while True:
    item = input("음식을 추가 하세요 : ")
    if item == 'q':
        break
    lunch.append(item)
set_lunch = set(lunch)

while True:
    print(set_lunch)
    item = input("음식을 삭제하세요 : ")
    if item == 'q':
        break
    set_lunch -= set([item])
print(set_lunch, "중에서 선택할게요")
for i in range(5,0,-1):
    print(i)
    time.sleep(1)
lunch = list(set_lunch)
result = random.choice(lunch)
print("오늘의 메뉴 : ",result)