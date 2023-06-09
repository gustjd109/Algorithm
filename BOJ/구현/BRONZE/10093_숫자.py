# 해당 문제는 고려해야할 두 가지 경우가 있다.
# 아래 경우를 모두 만족해야지 서브태스크를 통과하여 100점을 맞을 수 있다.
# 1) 입력받은 두 수의 크기 차이가 반대인 경우
#    - A가 B보다 크다면, A + 1부터 B 사이에 존재하는 수의 총 개수와 각 수를 출력
#    - B가 A보다 크다면, B + 1부터 A 사이에 존재하는 수의 총 개수와 각 수를 출력
# 2) 입력받은 두 수의 크기 차이가 1인 경우
#    - 먄약 A가 5이고 B가 6이면, 두 수의 크기 차이는 1
#    - 두 수 사이에 존재하는 수의 개수는 0이므로, 0을 출력하고 프로그램 종료
import sys

sys.stdin = open("input.txt","rt")
A, B = map(int, sys.stdin.readline().split())
min_value = min(A, B)
max_value = max(A, B)
num_cnt = max_value - min_value - 1

if max_value == min_value or min_value + 1 == max_value:
    num_cnt = 0
print(num_cnt)

for i in range(min_value + 1, max_value):
    print(i, end=' ')