"""
입력 조건
첫째 줄에 8 x 8 좌표 평면상에서 현제 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
입력 문자는 a1 처럼 열과 행으로 이뤄진다.

출력 조건
첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.
"""""""""
target = input()  # a1
row = int(target[1])  # 1
column = (int(ord(target[0])) - int(ord('a'))) + 1  # a
# row = Down, Up
# col = Left, Right
"""
steps 에서 모든 경우의 수를 체크 한다. 
U U L, U L L, D L L, D D L, D D R, D R R, U R R, U U R
"""
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:  # (-2, -1)
    # 이동 하고자 하는 위치 확인
    next_row = row + step[0]  # row = 1, step[0] = -2
    next_column = column + step[1]  # column = 1, step[1] = -1
    # 해당 위치로 이동이 가능 하다면 카운트 증가
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)
