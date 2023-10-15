"""
문제
2차원 평면 위의 점 N개가 주어진다.
좌표를 x좌표가 증가하는 순으로, x좌표가 같은면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N이 주어진다.
둘째 줄부터 N개의 줄에는 i번점의 위치 x와 y가 주어진다.
좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
"""
import sys
n = int(sys.stdin.readline())

lst = []
for i in range(n):
    # 2차원 리스트
    [a, b] = map(int, sys.stdin.readline().split())
    lst.append([a, b])

lst.sort()

for j in lst:
    print(j[0], j[1])
# n = int(input())
# x_lst = []
# y_lst = []
#
# for i in range(n):
#     x, y = list(map(int, input().split()))
#     x_lst.append(x)
#     y_lst.append(y)
#
# x_lst.sort()
# y_lst.sort()
#
# for x, y in zip(x_lst, y_lst):
#     print(x, y)
