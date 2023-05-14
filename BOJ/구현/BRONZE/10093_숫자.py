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