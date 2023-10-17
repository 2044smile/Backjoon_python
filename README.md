# coding_test_python
## 
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
