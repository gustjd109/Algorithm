import sys
from collections import deque

def bfs():
    # 큐가 비어있지 않다면 반복문 수행
    while queue:
        # 앞에서 찾은 익은 토마토의 높이, 가로, 세로 순서로 큐에서 삭제
        z, x, y = queue.popleft()
        
        # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 방향 순서로 익지 않은 토마토 탐색
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 좌표가 상자 범위를 벋어나지 않고, 해당 좌표의 토마토가 익지 않은 토마토라면 큐에 삽입하고 +1
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and box[nz][nx][ny] == 0:
                queue.append([nz, nx, ny])
                box[nz][nx][ny] = box[z][x][y] + 1

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 상자의 가로 칸의 수, 세로 칸의 수, 상자의 수 입력
    M, N, H = map(int, sys.stdin.readline().split())
    # 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보 입력
    box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

    # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 방향 정보
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    # 상자에 익은 토마토가 있으면 큐에 삽입
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 1:
                    queue.append([i, j, k])

    # BFS 수행
    bfs()

    result = 0
    # BFS 수행 완료 후, 박스에 익지 않은 토마토가 있으면 -1 반환하고 프로그램 종료
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    print(-1)
                    sys.exit(0)
                # 모두 익은 토마토만 있다면 익은 토마토 중에서 가장 큰 수를 결과값으로 반환
                else:
                    result = max(result, box[i][j][k])

    # 결과값 - 1이 최종 결과가 된다.
    print(result - 1)