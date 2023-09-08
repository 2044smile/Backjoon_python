# n, m, k를 공백을 기준으로 구분하여 입력 받기
# n 배열의 크기
# m 숫자가 더해지는 횟수
# k 연속해서 더하는 것을 제한
n, m, k = map(int, input().split())
# n개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기 *오름차순
first = data[-1] # 가장 큰 수
second = data[-2] # 두 번째로 큰 수

# 가장 큰 수가 더 해지는 횟수 계산
# m = 8, 숫자가 더 해지는 횟수
# k = 3, 연속해서 더하는 것을 제한한다.
count = m // (k + 1) * k
count += m % (k + 1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력