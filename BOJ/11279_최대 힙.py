import sys
import heapq

N = int(sys.stdin.readline())
Q = []
max_val = -sys.maxsize

for i in range(N):
    X = int(sys.stdin.readline())
    if X == 0:
        if not Q:
            print(0)
        else:
            print((-1)*heapq.heappop(Q))
    else:
        heapq.heappush(Q, (-1)*X)