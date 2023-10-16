"""
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다.
상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.
넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다.
이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
"""""""""
# 시간 초과
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())  # 10
# cards = list(map(int, input().split()))  # [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
# m = int(input())  # 8
# my_cards = list(map(int, input().split()))  # [10, 9, -5, 2, 3, 4, 5, -10]
# lst = []
#
# for i in my_cards:
#     if i in cards:
#         # 시간을 해결하기 위한 문제이므로 단순히 list의 메소드인 count 를 통해서 문제를 해결하는 것은 적절하지 않은 방법일 것이다.
#         lst.append(cards.count(i))
#     else:
#         lst.append(0)
#
# for j in lst:
#     print(j, end=" ")

# https://chancoding.tistory.com/45
# from sys import stdin
#
# _ = stdin.readline()  # 10
# # 오름차순, '이분 탐색'을 위해서 리스트 N을 순서대로 정렬
# N = sorted(map(int, stdin.readline().split()))  # [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
# _ = stdin.readline()  # 8
# M = map(int, stdin.readline().split())  # 10 9 -5 2 3 4 5 -10
#
#
# def binary(n, N, start, end):  # -10, [-10, -10, 2 ...], 0, 9 -> 3
#     if start > end:
#         return 0
#     m = (start+end) // 2  # m=4 | m=1
#     if n == N[m]:  # -10 == N[4]=3 | -10 == N[1]=-10
#         return N[start:end+1].count(n)  # N[0:1+1].count() -> 2
#     elif n < N[m]:  # -10 == N[4]=3 True, m=4-1=3 |
#         return binary(n, N, start, m-1)
#     else:
#         return binary(n, N, m+1, end)
#
# n_dic = {}  # 리스트 N에 있는 요소들이 각각이 몇개가 있는지를 dict에 담아서 저장
#
# for n in N:  # n=-10
#     start = 0  # 0
#     end = len(N) - 1  # 9
#     if n not in n_dic:
#         n_dic[n] = binary(n, N, start, end)  # {-10: 2}
#
# print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M))

# https://www.youtube.com/watch?v=QVoEbcK-eNI
# 1. hash 를 활용한 풀이 -> key와 value를 지정해야 한다. -> counting hash
import sys

input = sys.stdin.readline
N = int(input())
a = map(int, input().split())

# 1. hash에 num 개수 반영
hash = {}
for num in a:
    # 원래 있는 값을 가져와 달라 num 이라는 키가 존재하면 그 값을 가져오고, num이라는 키가 존재하지 않으면 0 을 반환
    hash[num] = hash.setdefault(num, 0) + 1

# 2. hash 에서 num 개수 출력
M = int(input())
b = map(int, input().split())
for num in b:
    print(hash.setdefault(num, 0), end=' ')
