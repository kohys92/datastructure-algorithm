n = 1260
count = 0

# checking the larger values of coins first in order.
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

# 거스름돈 문제는 그리디 알고리즘을 설명할 때 자주 소개된다. 문제는 다양하지만 접근 방식은 유사하다.