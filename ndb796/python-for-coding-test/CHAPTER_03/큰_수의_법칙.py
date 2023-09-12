# n, m, k를 공백을 기준으로 구분하여 입력 받기
# n 배열의 크기
# m 숫자가 더해지는 횟수
# k 연속해서 더하는 것을 제한
n, m, k = map(int, input().split())  # 5 7 3
data = list(map(int, input().split()))  # 2 4 5 4 6

data.sort()  # 2 4 4 5 6
first = data[-1]  # 6
second = data[-2]  # 5

# 가장 큰 수가 더 해지는 횟수 계산
count = m // (k + 1) * k  # 7 // 4 = 1 * 3 => 3
count += m % (k + 1)  # 7 % 4 => 3 ==> count = 6
# count = m // (k + 1) * k
# 반복되는 수열의 길이는 (k + 1) 입니다.
# 따라서, m 을 (k + 1)로 나눈 몫은 수열이 반복되는 횟수가 됩니다.
# 여기에 k를 곱해주면, 가장 큰 수가 등장하는 횟수가 됩니다.

# count += m % (k + 1)
# 이 때 m 이 (k + 1)로 나누어 떨어지지 않는 경우도 고려해야 합니다.
# 그럴 때는 m 을 (k + 1) 로 나눈 나머지를 추가로 더해줍니다.

result = 0
result += count * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)  # 최종 답안 출력  # 6 6 6 5 6 6 6
