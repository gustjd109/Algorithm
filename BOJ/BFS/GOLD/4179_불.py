# 참고 풀이 : https://hangjastar.tistory.com/262
import sys
from collections import deque

def bfs(queue, visited):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0 and maze[nx][ny] != '#':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    return visited

if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().split())
    maze = [list(sys.stdin.readline().strip()) for _ in range(R)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    jQueue, fQueue = deque(), deque()
    jVisited, fVisited = [[0] * C for _ in range(R)], [[0] * C for _ in range(R)]
    minTime = 2001

    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'J':
                jQueue.append((i, j))
                jVisited[i][j] = 1
            elif maze[i][j] == 'F':
                fQueue.append((i, j))
                fVisited[i][j] = 1

    jVisited = bfs(jQueue, jVisited)
    fVisited = bfs(fQueue, fVisited)

    for i in range(R):
        for j in range(C):
            if jVisited[i][j] > 0:
                if jVisited[i][j] < fVisited[i][j] or fVisited[i][j] == 0:
                    if i == 0 or j == 0 or i == R - 1 or j == C - 1:
                        minTime = min(minTime, jVisited[i][j])

    print(minTime if minTime != 2001 else "IMPOSSIBLE")