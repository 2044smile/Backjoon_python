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
# Tim
import sys

input = sys.stdin.readline

n = input()
n_lst = list(map(int, input().split()))

m = input()
m_lst = list(map(int, input().split()))

for i in m_lst:
    if i in n_lst:
        print('yes')
    else:
        print('no')

