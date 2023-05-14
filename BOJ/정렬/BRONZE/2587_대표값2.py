import sys

sys.stdin = open("input.txt","rt")
N = sorted([int(sys.stdin.readline()) for _ in range(5)])
print(sum(N) // 5, N[2], sep="\n")