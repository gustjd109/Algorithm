import sys

sys.stdin = open("input.txt","rt")
S = sys.stdin.readline()
i = int(sys.stdin.readline())
print(S[i - 1])