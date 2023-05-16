import sys

sys.stdin = open("input.txt","rt")
T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().strip().split())
    print(A + B)