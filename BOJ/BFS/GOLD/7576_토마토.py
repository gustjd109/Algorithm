import sys
from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and tomatoBox[nx][ny] == 0:
                tomatoBox[nx][ny] = tomatoBox[x][y] + 1
                queue.append((nx, ny))

if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split())
    tomatoBox = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    for i in range(N):
        for j in range(M):
            if tomatoBox[i][j] == 1:
                queue.append((i, j))

    bfs()

    maxDay = 0
    for row in tomatoBox:
        for i in row:
            if i == 0:
                print(-1)
                exit(0)
        maxDay = max(maxDay, max(row))

    print(maxDay - 1)