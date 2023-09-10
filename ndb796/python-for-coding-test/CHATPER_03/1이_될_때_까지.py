"""cslee 정답
1. N이 K의 배수가 될 때 까지 1씩 빼기
2. N을 K로 나누기

최종
N이 1이 될 때 까지 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.
"""
n, k = map(int, input().split())
result = 0

while n >= k:
    calc = n / k
    target = calc.is_integer()

    if target:
        n = n / k
        result += 1
    else:
        n -= 1
        result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

# 3-6.py 답안 예시
# N, K을 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:  # 나머지가 0이 아니라면
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)
