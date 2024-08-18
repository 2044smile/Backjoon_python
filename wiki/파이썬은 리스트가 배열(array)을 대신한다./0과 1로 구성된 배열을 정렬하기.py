"""
문제 설명

0과 1로 이루어진 배열이 있다.
배열 자체를 오름차순으로 정렬하라.

입력: [1, 0, 1, 1, 1, 1, 1, 0, 0, 0], 출력: [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
입력: [1, 1], 출력: [1, 1]
"""
def ascendingOrder(target):
    target.sort()
    print(target)


ascendingOrder(target=[1, 0, 1, 1, 1, 1, 1, 0, 0, 0])
