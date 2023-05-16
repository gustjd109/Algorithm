import sys

sys.stdin = open("input.txt","rt")
N = int(sys.stdin.readline())
for i in range(N, 0, - 1):
    print((' ' * (N - i)) + ('*' * (2 * i - 1)))