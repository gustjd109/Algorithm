import sys

sys.stdin = open("input.txt","rt")
A, B = map(int, sys.stdin.readline().split())
A_Set = set(map(int, sys.stdin.readline().split()))
B_Set = set(map(int, sys.stdin.readline().split()))
print(len(A_Set - B_Set) + len(B_Set - A_Set))