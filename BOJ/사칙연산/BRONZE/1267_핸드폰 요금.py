import sys

sys.stdin = open("input.txt","rt")
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
Y = M = 0
for i in range(N):
    Y += (N_list[i] // 29 + 1) * 10
    M += (N_list[i] // 60 + 1) * 15
if Y == M:
    print('Y M', Y)
elif Y < M:
    print('Y', Y)
else:
    print('M', M)