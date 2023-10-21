"""
입력 조건
첫째 줄에는 공백으로 구분하여 N개의 정수가 주어진다.
둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다.
이때 정수는 1보다 크고 1,000,000 이하이다.
셋째 줄에는 정수 M이 주어진다
넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다.

출력 조건
첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.
"""""""""
# 이진 탐색 소스코드 구현
import sys

input = sys.stdin.readline

# N(가게의 부품 개수) 입력
n = int(input())  # 5
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))  # 8 3 7 9 2
array.sort()  # 이진 탐색을 수행하기 위해 사전에 정렬 수행  2 3 7 8 9

# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())  # 3
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))  # 5 7 9


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:  # 5 7 9
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
