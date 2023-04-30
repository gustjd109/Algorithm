import sys
from collections import deque
sys.setrecursionlimit(10**9)

def BFS(x, y):
    # 집 하나를 찾았기 때문에 집 카운트 개수 1로 초기화
    cnt = 1
    queue = deque()
    # 큐에 찾은 집의 정보 삽입
    queue.append((x, y))
    # 찾은 집 방문 체크
    visited[x][y] = True
    # 큐가 비어있을 때까지 반복문 수행
    while queue:
        # 찾은 집의 정보 삭제
        x, y = queue.popleft()
        # 찾은 집의 상하좌우 방향 탐색
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 찾은 집의 상화좌우 방향에 있는 데이터 중에서 지도의 크기를 넘어가지 않고, 방문하지 않았고, 집인 경우 큐에 찾은 집 삽입하고 방문체크
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and house_map[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                # 집을 하나 찾았기 때문에 집 카운트 개수 1증가
                cnt += 1
    # 반복문 수행을 완료한 뒤, 집 카운트 개수 반환
    return cnt

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 지도의 크기 N 입력
    N = int(sys.stdin.readline())
    # N X N 지도에 집이 있는 곳 입력
    house_map = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    # 집 방문 체크
    visited = [[False for _ in range(N)] for _ in range(N)]
    # 단지별 집 개수 카운트 정보 리스트
    result = []
    # 상하좌우 방향 정보
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 지도에서 방문하지 않고, 값이 1인(집인 경우) 인덱스에 대해서 BFS 수행
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False and house_map[i][j] == 1:
                # BFS 수행 완료 후, 반환된 집 카운트 개수 정보를 리스트에 삽입
                result.append(BFS(i, j))
    
    # 단지별 집 개수 정보 리스트 길이 출력
    print(len(result))
    # 단지별 집 개수 정보 리스트 오름차순 정렬
    result.sort()
    # 정렬된 단지별 집 개수 정보 리스트 출력
    for i in range(len(result)):
        print(result[i])