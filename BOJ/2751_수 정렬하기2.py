import sys

N = int(sys.stdin.readline())
Num = []

for i in range(N):
    Num.append(int(sys.stdin.readline()))

Num.sort()

for i in (Num):
    print(i)