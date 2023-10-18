"""
입력 조건
첫째 줄에 수열에 속해 있는 수의 갯후 N이 주어진다.
둘째 줄부터 N + 1 번째 줄까지 N개의 수가 입력된다.

출력 조건
입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다.
"""""""""
n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

for _ in lst:
    print(_, end=' ')
