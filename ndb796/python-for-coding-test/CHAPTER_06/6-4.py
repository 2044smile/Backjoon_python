# 퀵 정렬
# 1. 제일 앞에 있는 값을 pivot 값으로 설정한다.
# 1-1. 왼쪽에서는 pivot 값보다 큰 값들을 찾고,
# 1-2.오른쪽에서는 pivot 값보다 작은 값들을 찾는다.
# 2. 그리고 큰 값과 작은 값을 변경한다. 왜냐하면 큰 값은 오름차순으로 설정된다.
# 3. 만약 충돌이 발생하는 경우에는 더 작은 값과 pivot 에 있는 값을 변경한다.
# 3-1. pivot 에 원려 있었던 값을 고정 값이다.
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)