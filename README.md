# coding_test_python

## remind
1. 파이썬 for 문 enumerate() 활용
```python
for index, i in enumerate(range(5), start=1):
    print(index, i)
```
2. 파이썬 for 문
```python
for k in range(0, len(lst), 3):
    group = lst[k:k+3]
    print(' '.join(map(str, group)))
```