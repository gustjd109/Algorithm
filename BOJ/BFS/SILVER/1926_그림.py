import sys
from collections import deque

def bfs(board, a, b):
    queue = deque() # 큐 생성
    queue.append((a, b)) # 큐에 (a, b)좌표 추가
    board[a][b] = 0 # 방문 좌표 방문 처리
    pictureSize = 1 # 그림 넓이 1로 초기화

    while queue:
        x, y = queue.popleft() # 큐에서 방문 좌표 삭제
        for i in range(4): # 네 방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M: # 좌표가 범위를 벗어난다면 무시
                continue
            if board[nx][ny] == 1: # (nx, ny)좌표 값이 1이면, 해당 좌표 방문 처리/큐에 삽입/그림 넓이 값 +1
                board[nx][ny] = 0
                queue.append((nx, ny))
                pictureSize += 1
    
    return pictureSize # 그림 넓이 반환

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split()) # 도화지 세로 가로 크기 입력
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 도화지에 그림 정보 입력

    # 상, 하, 좌, 우 좌표 정보
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    pictureCnt = [] # 그림 개수를 저장하는 배열 초기화

    # 도화지의 세로 가로를 모두 탐색하면서 그림 개수와 넓이 구하기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                pictureCnt.append(bfs(board, i, j))

    # 그림 개수가 있으면 그림 개수와 그 중 가장 넓은 그림의 넓이 출력하고, 아니면 0 출력
    if len(pictureCnt) != 0:
        print(len(pictureCnt))
        print(max(pictureCnt))
    else:
        print(len(pictureCnt))
        print(0)