# coding_test_python
## 이것이 코딩 테스트다.
* CHAPTER_03 그리디: 현재 상황에서 가장 좋아 보이는 것만을 선택하는 알고리즘
* CHAPTER_04 구현: 머릿속에 있는 알고리즘을 정확하고 빠르게 프로그램으로 작성하기
* CHAPTER_05 DFS/BFS: 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘
* CHAPTER_06 정렬: 연속된 데이터를 기준에 따라서 정렬하기 위한 알고리즘
* CHAPTER_07 이진 탐색: 탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘
## remind
1. for 문 enumerate() 활용
```python
for index, i in enumerate(range(5), start=1):
    print(index, i)
```
2. for 문
```python
for k in range(0, len(lst), 3):
    group = lst[k:k+3]
    print(' '.join(map(str, group)))
```
3. setdefault
```python
hash = {}
hash[num] = hash.setdefault(num, 0)  # hash 안에서 num 이라는 값이 존재하면 그 값을 보여주고, 없다면 0을 반환한다.
```
