# 값을 하나씩 입력받아 비교를 통해 최대값과 최대값의 인덱스를 찾는 풀이
import sys

sys.stdin = open("input.txt","rt")
max_num = -sys.maxsize
max_num_idx = 0
for i in range(9):
    N = int(sys.stdin.readline())
    if N > max_num:
        max_num = N
        max_num_idx = i + 1
print(max_num, max_num_idx, sep='\n')

# 값을 한번에 입력받아 리스트에 저장 후, 
# 파이썬의 max와 index 함수를 이용하여 최대값과 최대값의 인덱스를 찾는 풀이
import sys

sys.stdin = open("input.txt","rt")
N = [int(input()) for i in range(9)]
print(max(N))
print(N.index(max(N)) + 1)