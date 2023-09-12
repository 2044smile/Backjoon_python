# cslee
row, column = map(int, input().split())  # 행, 열

result = []

for i in range(row):
    data = list(map(int, input().split()))
    result.append(data[0])

result.sort()
print(result[-1])


# 3-3.py min() 함수를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))

    # 현재 줄에서 '가장 작은 수 찾기'
    min_value = min(data)

    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

# 3-4.py 2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))

    min_value = 10001  # 조건에서 10,000 이하라고 표시되어있음
    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)

print(result)
