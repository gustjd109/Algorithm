import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    dq = deque(sys.stdin.readline().strip()[1:-1].split(','))

    if n == 0:
        dq = []

    rCount = 0
    isError = False

    for i in p:
        if i == 'R':
            rCount += 1
        else:
            if not dq:
                isError = True
                break
            else:
                if rCount % 2 == 1:
                    dq.pop()
                else:
                    dq.popleft()

    if isError == True:
        print('error')
    else:
        if rCount % 2 == 1:
            dq.reverse()
            print('[' + ','.join(dq) + ']')
        else:
            print('[' + ','.join(dq) + ']')