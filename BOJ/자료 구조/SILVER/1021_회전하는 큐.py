import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
popNumPosition = list(map(int, sys.stdin.readline().split()))
rotatingDeque = deque([i for i in range(1, N + 1)])
count = 0

for i in popNumPosition:
    while True:
        if rotatingDeque[0] == i:
            rotatingDeque.popleft()
            break
        else:
            if rotatingDeque.index(i) < len(rotatingDeque) / 2:
                while rotatingDeque[0] != i:
                    rotatingDeque.rotate(-1)
                    count += 1
            else:
                while rotatingDeque[0] != i:
                    rotatingDeque.rotate(1)
                    count += 1

print(count)