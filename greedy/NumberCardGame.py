# 3 숫자 카드 게임 페이지 96
# 그리디 문제

# 입력 예시 1
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 출력 예시 1
# 2

# 입력 예시 2
# 2 4
# 7 3 1 8
# 3 3 3 4

# 출력 예시 2
# 3

# N, M 을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)  # 최종 답안 출력


