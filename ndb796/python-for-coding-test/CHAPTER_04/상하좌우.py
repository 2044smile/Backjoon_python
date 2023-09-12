"""
입력 조건
첫째 줄에 공간의 크기를 나타내는 N이 주어진다.
둘쨰 줄에 여행가 A가 이동할 계획서 내용이 주어진다.

출력 조건
첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력한다.
"""
# cslee
N = int(input())  # 상하좌우 공간의 크기를 입력 N X N
plan = input().split()

x, y = 1, 1  # default

for i in plan:
    if i == 'L':
        if y == 1:
            continue
        else:
            y -= 1
    if i == 'R':
        if y == 5:
            continue
        else:
            y += 1
    if i == 'U':
        if x == 1:
            continue
        else:
            x -= 1
    if i == 'D':
        if x == 5:
            continue
        else:
            x += 1

print(x, y)

# 4-1.py 답안 예시
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:  # plans = ['R', 'R', 'R', 'U', 'D', 'D'
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):  # 'L' 'R' 'U' 'D'
        if plan == move_types[i]:
            nx = x + dx[i]  # if 결과 i = 1, dx[1] 이라는 값 0을 가져온다.
            ny = y + dy[i]  # if 결과 i = 1, dy[1] 이라는 값 1을 가져온다. 즉 'R' 이 3번 나오기 때문에 nx=1, ny=4가 된다.
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:  # 즉 nx,ny 0이라는 값이 저장되어 있다면 그것은 생략하고 넘어간다.
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)