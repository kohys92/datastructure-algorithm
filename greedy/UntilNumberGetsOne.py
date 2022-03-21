

n, k = map(int, input().split())
count = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K 로 나누어 떨어진다면 N을 K로 나누기
    if n % k == 0:
        n = n / k
        count += 1

    # 나누어 떨어지지 않는다면 N에서 1씩 빼기
    else:
        n -= 1
        count += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    count += 1

print(count)