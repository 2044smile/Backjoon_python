# def find_sub_array(arr: list[int], s: int) -> list[int]:
#     """배열 arr에서 연속한 원소의 합이 s인 부분 배열의 인덱스를 구한다.
#     Arguments:
#         arr (list[int]): 양의 정수
#         s: 부분 배열의 합
#     Return:
#         list[int]: 부분 배열의 인덱스, 조건을 만족하는 부분 배열이 없으면 [-1]
#      """
#     for i in range(len(arr)):
#         sub_total: int = 0
#         for j in range(i, len(arr)):
#             sub_total += arr[j]
#             if sub_total == s:
#                 return [i+1, j+1]
#     return [-1]


# # Test code
# sample1 = ([1, 2, 3, 7, 5], 12)
# sample2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
# for arr, s in (sample1, sample2):
#     print(find_sub_array(arr, s))
# 포인터 두 개를 이용하기
def find_sub_array(arr: list[int], s: int) -> list[int]:
    left: int = 0
    sub_total: int = 0

    for right in range(len(arr)):
        sub_total += arr[right]
        while left < right and sub_total > s:
            sub_total -= arr[left]
            left += 1
        if sub_total == s:
            return [left+1, right+1]
    return [-1]

sample1 = ([1, 2, 3, 7, 5], 12)
sample2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
sample3 = ([1, 2, 3, 4], 0)
for arr, s in (sample1, sample2, sample3):
    print(find_sub_array(arr, s))