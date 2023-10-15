"""
문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫쨰 줄에 N이 주어진다.
둘쨰 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
"""
import sys

input = sys.stdin.readline

n = int(input())  # 6  # 5
lst = list(map(int, input().split()))  # 1000 999 1000 999 1000 999  # 2 4 -10 4 -9
lst2 = sorted(list(set(lst)))  # 999 1000  # -10 -9 2 4

dic = {lst2[i]: i for i in range(len(lst2))}
# {-10: 0, -9: 1, 2: 2, 4: 3}
for i in lst:  # -10 -9 2 4 4
    print(dic[i], end=' ')
