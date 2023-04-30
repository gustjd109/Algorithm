# DFS를 사용하지 않은 풀이
import sys

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 방 바닥의 세로 크기 N과 가로 크기 M 입력
    N, M = map(int, sys.stdin.readline().split())
    # 방 바닥 장식 모양 정보 입력
    floor_decoration_shape = [list(sys.stdin.readline().strip()) for _ in range(N)]
    # 방 바닥을 장식하는데 필요한 나무 판자의 개수 0으로 초기화
    cnt = 0

    # '-' 모양의 바닥 장식 개수 세기
    for i in range(N):
        shape = ''
        for j in range(M):
            if floor_decoration_shape[i][j] == '-':
                if floor_decoration_shape[i][j] != shape:
                    cnt += 1
            shape = floor_decoration_shape[i][j]

    # '|' 모양의 바닥 장식 개수 세기
    for j in range(M):
        shape = ''
        for i in range(N):
            if floor_decoration_shape[i][j] == '|':
                if floor_decoration_shape[i][j] != shape:
                    cnt += 1
            shape = floor_decoration_shape[i][j]

    print(cnt)

# DFS를 이용한 풀이
import sys
sys.setrecursionlimit(10**9)

def DFS(x, y):
    # 바닥 장식이 '-'일 경우
    if floor_decoration_shape[x][y] == '-':
        # 찾은 바닥 방문처리
        floor_decoration_shape[x][y] = 1
        # 바닥 범위를 벗어나지 않고, 장식이 '-'인 좌우 바닥 탐색하여 DFS 수행
        for _y in [1, -1]:
            ny = y + _y
            if 0 <= ny < M and floor_decoration_shape[x][ny] == '-':
                DFS(x, ny)

    # 바닥 장식이 '|'일 경우
    if floor_decoration_shape[x][y] == '|':
        # 찾은 바닥 방문처리
        floor_decoration_shape[x][y] = 1
        # 바닥 범위를 벗어나지 않고, 장식이 '|'인 좌우 바닥 탐색하여 DFS 수행
        for _x in [1, -1]:
            nx = x + _x
            if 0 <= nx < N and floor_decoration_shape[nx][y] == '|':
                DFS(nx, y)

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 방 바닥의 세로 크기 N과 가로 크기 M 입력
    N, M = map(int, sys.stdin.readline().split())
    # 방 바닥 장식 모양 정보 입력
    floor_decoration_shape = [list(sys.stdin.readline().strip()) for _ in range(N)]
    # 방 바닥을 장식하는데 필요한 나무 판자의 개수 0으로 초기화
    cnt = 0

    # 방 바닥을 모두 탐색하면서 장식이 '-' 또는 '|'인 것을 찾아 DFS 수행
    # DFS 수행을 완료할 떄마다 카운트 1증가
    for i in range(N):
        for j in range(M):
            if floor_decoration_shape[i][j] == '-' or floor_decoration_shape[i][j] == '|':
                DFS(i, j)
                cnt += 1

    print(cnt)