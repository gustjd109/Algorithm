import sys
from collections import deque

# bfs함수 정의
def bfs(x, y, height):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    # 현재 노드 큐에 삽입
    queue.append((x, y))
    # 현재 노드 방문 처리
    visited[x][y] = 1

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 노드 꺼내기
        x, y = queue.popleft()
        # 상하좌우 인접 노드 검색
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 상하좌우 인점 노드 검색 시, 행렬 범위 넘어가는지 확인
            if 0 <= nx < n and 0 <= ny < n:
                # graph[nx][ny]값이 비가 온 높이값보다 크고, 방문하지 않은 상태인지 확인
                if visited[nx][ny] == False and graph[nx][ny] > height:
                    # 위 조건에 만족하는 상하좌우로 탐색된 인접 노드 큐에 삽입 및 방문 처리
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 행과 열의 개수를 나타내는 n 입력
n = int(sys.stdin.readline())

# 지역 높이 정보 입력
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
# 입력받은 지역 높이 중 최대 높이 찾기(0부터 최대 높이 - 1까지 탐색)
max_height = 0
for i in range(n):
    for j in range(n):
        if max_height < graph[i][j]:
            max_height = graph[i][j]

# 방향 정보(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 0부터 지역 최대 높이 - 1별로 탐색된 최대 안전 지역 수 저장
result = []

# 비가온 높이를 0부터 지역 최대 높이 - 1만큼 반복문 수행
for i in range(max_height):
    # 안전 지역 카운트
    safezone_cnt = 0
    # 방문 체크
    visited = [[False] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            # graph[j][k]값이 비가온 높이값보다 크고, 방문하지 않은 상태인지 확인
            if graph[j][k] > i and visited[j][k] == False:
                # 위 조건을 만족하면, bfs함수 실행(매개변수로 현재 (x, y)좌표와 비가온 높이값 전달)
                bfs(j, k, i)
                # bfs함수가 모두 종료되면, 안전 지역을 하나 찾았다는 의미로 안전 지역 카운트 +1
                safezone_cnt += 1
    # 한번의 비가온 높이 반복문 수행 완료 후, 해당 높이의 최대 안전 지역 카운트를 리스트에 저장
    result.append(safezone_cnt)

# 결과 출력
print(max(result))