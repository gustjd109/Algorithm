import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
Q = deque([i for i in range(1, N + 1)])
answer = []

while Q:
    for i in range(K - 1):
        Q.append(Q.popleft())
    answer.append(str(Q.popleft()))

print("<", end='')
print(*answer, sep=", ", end='')
# print(', '.join(answer), end='') # 요것도 OK
print(">")