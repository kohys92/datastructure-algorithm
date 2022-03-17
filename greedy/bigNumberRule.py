# 실전문제 p.g 92 - 큰 수의 법칙

# 입력 예시
# 5 8 3
# 2 4 5 4 6

# 출력 예시
# 46

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N 개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()   # 입력받은 수들 정력하기
first = data[n-1]  # 가장 큰 수
second = data[n-2]  # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:  # m이 0이라면 반복문 탈출
        break
    result += second  # 두 번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print(result)  # 최종 답안 출력


# M 의 크기가 100억 이상일 때 위의 방법은 시간 초과가 된다.

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N 개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()   # 입력받은 수들 정력하기
first = data[n-1]  # 가장 큰 수
second = data[n-2]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)