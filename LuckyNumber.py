import random

luckyNumer = []

for i in range(6):
    random_number = random.randint(1, 45)
    luckyNumer.append(random_number)

luckyNumer.sort()

for j in luckyNumer:
    print(j , end=' ')
    