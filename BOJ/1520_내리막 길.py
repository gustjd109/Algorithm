import sys
sys.setrecursionlimit(10**9)

def dfs(x, y):
    # 목적지에 도착했으면 1을 리턴하고, 목적지까지 이동한 모든 칸에 1증가
    if x == M - 1 and y == N - 1:
        return 1
    
    # 방문하지 않은 곳이라면 방문처리
    if dp[x][y] == -1:
        dp[x][y] = 0
        
        # 방문하지 않은 곳에서 상하좌우 탐색
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            # nx와 ny값이 지도 범위 내에 있고, 현재 높이보다 낮은 높이라면
            if 0 <= nx < M and 0 <= ny < N and travel_map[nx][ny] < travel_map[x][y]:
                # (nx, ny) 지점에서 DFS 재귀호출
                dp[x][y] += dfs(nx, ny)
    
    # 탐색한 곳이거나 탐색할 수 없는 곳이라면 자기 자신을 리턴
    # 마지막에 dp테이블의 (0, 0) 값을 리턴
    return dp[x][y]

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 지도의 가로, 세로 크기 입력
    M, N = list(map(int, sys.stdin.readline().split()))
    # 지도의 각 지점의 높이 입력
    travel_map = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    # dp테이블 -1로 초기화
    dp = [[-1 for _ in range(N)] for _ in range(M)]
    # 방향 정보(상하좌우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # DFS 함수 수행
    print(dfs(0, 0))
    