from collections import deque
import sys

def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    
    queue.append((x, y))
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 (x, y) 좌표 하나 삭제
        x, y = queue.popleft()
        # 현재 위치에서 상하좌우 녜 방향으로의 이동 가능 위치 확인
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # N X M 공간을 벗어난 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 좌표를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 현재 좌표가 (N -1, M -1)일 때 최단 거리 값 반환
    return graph[N - 1][M - 1]

if __name__ == "__main__":
    # N X M 크기의 배열을 표현하는 두 정수 입력
    N, M = map(int, sys.stdin.readline().split())
    # 미로를 표현하는 N개의 줄에서 M개의 정수 입력
    graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    # 방향 정보(상하좌우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # (0, 0) 좌표부터 BFS 탐색 시작
    print(bfs(0, 0))