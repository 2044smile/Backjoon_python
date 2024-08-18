"""
문제 설명

정수로만 이루어진 배열이 주어질 때, 가장 큰 두 수를 찾아 [가장 큰 값, 둘째로 큰 값] 을 반환하는 함수를 완성하라.

입력: [3, -1, 5, 0, 7, 4, 9, 1], 출력: [9, 7]
입력: [7], 출력: [7]

쉽게 떠올릴 수 있는 방법은 배열을 내림차순으로 정렬 한 후에 앞의 두 수를 가져오는 것이다.
그러나 여기서는 배열의 인덱싱과 원소를 비교하는 방법으로 해결한다.
"""
def find_max_two(arr: list[int]) -> list[int]:
    if len(arr) < 2:  # arr 가 1개 일 때는 return arr
        return arr
    max1, max2 = arr[:2]  # 초기값 설정, 코드 간결성, 효율성
    if max2 > max1:
        max1, max2 = max2, max1
    for i in arr[2:]:
        if i > max1:
            max1, max2 = i, max1
        elif i > max2:
            max2 = i
    
    return [max1, max2]
        
# Test code
arr = [[3, -1, 5, 0, 7, 4, 9, 1], [7]]
for a in arr:
    print(f"{a}에서 가장 큰 두 값: {find_max_two(a)}")