"""
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄부터 N개의 줄에는 수가 주어진다.
이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

lst.sort()

for j in lst:
    print(j)
# https://0ver-grow.tistory.com/412
# 버블정렬로 정렬하기
# N = int(input())
# M = []
#
# for i in range(N):
#     M.append(int(input()))
#
# # Bubble Sort
# for i in range(len(M)):
#     print('i : ', i)
#     print('M[i] : ', M[i])
#     for j in range(len(M)):
#         print('j : ', j)
#         print('M[j] : ', M[j])
#         if M[i] < M[j]:
#             M[i], M[j] = M[j], M[i]  # 5 2 3 4 1 | 2 5 3 4 1 | 2 3 5 4 1 | 2 3 4 5 1 | 1 2 3 4 5
#             print(M)
#
# for n in M:
#     print(n)
# https://0ver-grow.tistory.com/412
# 삽입정렬로 정렬하기
# N = int(input())
# M = []
#
# for i in range(N):
#     M.append(int(input()))
#
# # Insert Sort
# for i in range(1, len(M)):  # 1, 2, 3, 4
#     while (i > 0) & (M[i] < M[i-1]):  # 5 2 3 4 1 | 2 5 3 4 1 | 2 3 5 4 1 | 2 3 4 5 1 | 1 2 3 4 5
#         M[i], M[i-1] = M[i-1], M[i]  # EX] 앞에 있는 값들을 체크한다. i 값이 1이라면 M[i-1] 0 까지 검사한다.
#         i -= 1
#
# for n in M:
#     print(n)
