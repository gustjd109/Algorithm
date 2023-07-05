import sys

sys.stdin = open("input.txt","rt")
A, B = map(int, sys.stdin.readline().split())
A_List = list(map(int, sys.stdin.readline().split()))
B_List = list(map(int, sys.stdin.readline().split()))
print(*sorted(A_List + B_List))