import sys

sys.stdin = open("input.txt","rt")
N_list = list(map(int, sys.stdin.readline().split()))
result = 0
for i in N_list:
    result += i * i
print(result % 10)