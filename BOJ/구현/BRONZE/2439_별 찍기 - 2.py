import sys

sys.stdin = open("input.txt","rt")
N = int(sys.stdin.readline())
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i)