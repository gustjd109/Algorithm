import sys

N, X = map(int, sys.stdin.readline().split())
A = map(int, sys.stdin.readline().split())

for i in A:
    if i < X:
        print(i, end=' ')