"""
입력 조건
첫 번째 줄에 학생의 수 N이 입력된다.
두 번째 줄부터 N + 1 번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.

출력 조건
모든 학생의 이름을 성적이 낮은 순서대로 출력한다.
성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.
"""""""""
n = int(input())
lst = []

for _ in range(n):
    lst.append(input().split())

lst.sort(key=lambda x: x[1])

for _ in lst:
    print(_[0], end=' ')

# 6-11.py 답안 예시
n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()  # split 해서 데이터를 받고
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))  # str와 int를 분리하여 저장

# 키를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
