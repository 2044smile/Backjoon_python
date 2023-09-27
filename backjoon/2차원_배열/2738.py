"""
문제
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다.
둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다.
행렬의 각 원소는 공백으로 구분한다.
"""
# 런타임 에러 발생
n, m = map(int, input().split())
first = [list(map(int, input().split())) for _ in range(n)]
second = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    for j in range(m):
        print(first[i][j] + second[i][j], end=' ')
    print()
#
# for k in range(0, len(lst), 3):
#     group = lst[k:k+3]
#     print(' '.join(map(str, group)))
# 런타임 에러가 발생하여 https://develop247.tistory.com/93 참고
# first, second 가 아래 코드의 A, B 역할을 하고 있다.
# 질문 url https://www.acmicpc.net/board/view/127360
# A, B = [], []
#
# N, M = map(int, input().split())
#
# for row in range(N):
#     row = list(map(int, input().split()))
#     A.append(row)
#
# for row in range(N):
#     row = list(map(int, input().split()))
#     B.append(row)
#
# for row in range(N):
#     for col in range(M):
#         print(A[row][col] + B[row][col], end=' ')
#     print()
