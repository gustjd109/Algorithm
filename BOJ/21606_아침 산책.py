import sys
sys.setrecursionlimit(10**9)

# DFS 함수 : V는 정점의 번호, cnt는 실외와 연결된 실내 노드 개수 카운트
def dfs(v, cnt):
    visited[v] = True

    # 노드 V와 연결된 인접 노드를 하나씩 가져옴
    for i in graph[v]:
        # 해당 노드의 위치가 실내이면 실내 카운트 +1
        if location[i] == 1:
            cnt += 1
        # 방문하지 않았고 i번째 노드의 위치가 실외라면 해당 실외를 기준으로 DFS 수행
        elif not visited[i] and location[i] == 0:
            cnt = dfs(i, cnt)
    return cnt

if __name__ == "__main__":
    ans = 0
    # 정점 개수 입력
    N = int(sys.stdin.readline())
    # 1과 0으로 이루어진 실내, 실외 정보 입력 : 인덱스 번호를 1부터 시작하기 위해 앞에 0으로 설정
    location = [0] + list(map(int, sys.stdin.readline().strip()))
    # 1번 노드부터 N번 노드까지 받아오기 위한 빈 공간 생성
    graph = [[] for _ in range(N + 1)]

    # 간선 정보 입력
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        # 둘 노드가 실내라면 서로 방문하는 케이스가 2가지이므로 +2
        if location[a] == 1 and location[b] == 1:
            ans += 2

    sum = 0
    visited = [False] * (N + 1)
    for i in range(1, N + 1):
        # 실외를 기준으로 dfs 실행
        if not visited[i] and location[i] == 0:
            # 현재 cnt는 0으로 설정
            x = dfs(i, 0)
            # 실외인 노드를 기준으로 인접 노드의 개수를 세는 것이 N * (N - 1)이므로 실외 노드 걸릴때마다 전부 세기
            sum += x * (x - 1)

    print(sum + ans)