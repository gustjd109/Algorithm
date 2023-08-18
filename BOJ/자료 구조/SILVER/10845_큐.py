import sys
from collections import deque

N = int(sys.stdin.readline())
Q = deque([])

for i in range (N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        Q.append(cmd[1])
    elif cmd[0] == 'pop':
        if not Q:
            print(-1)
        else:
            print(Q.popleft())
    elif cmd[0] == 'size':
        print(len(Q))
    elif cmd[0] == 'empty':
        if not Q:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if not Q:
            print(-1)
        else:
            print(Q[0])
    elif cmd[0] == 'back':
        if not Q:
            print(-1)
        else:
            print(Q[-1])