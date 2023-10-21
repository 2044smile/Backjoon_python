# 계수 정렬
import sys

input = sys.stdin.readline
# N(가게의 부품 개수)을 입력받기
n = int(input())  # 5
# 리스트를 전부 0으로 초기화
array = [0] * 1000000

# 가계에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():  # 8 3 7 9 2
    # array[8] = 1 주어진 값의 인덱스에 접근하여 value 를 1로 변경
    array[int(i)] = 1

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())  # 3
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))  # 5 7 9

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
