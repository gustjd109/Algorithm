import sys

sys.stdin = open("input.txt","rt")
A, B = map(int, sys.stdin.readline().split())
print(A + B)