"""
문제
9x9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때,
이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

입력
첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다.
주어지는 수는 100보다 작은 자연수 또는 0이다.

출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다.
최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.
"""
row = []
max_values, max_index = [], []

for i in range(9):  # 행
    for j in range(1, 9, 9):  # 열
        row.append(list(map(int, input().split())))

for index, k in enumerate(row):
    max_values.append(max(k))  # 최댓값
    max_index.append(k.index(max(k)))

# max_values EX] [85, 88, 87, 85, '90', 87, 89, 70, 87] => 90
# max_values 행에서 몇번 째에 위치해 있는 지 EX] max_values.index(max(max_values)) + 1 => 5
#            열에서                          EX] max_index[max_values.index(max(max_values))] + 1 => 7
print(max(max_values))
print(max_values.index(max(max_values)) + 1, max_index[max_values.index(max(max_values))] + 1)  # 5행 7열
