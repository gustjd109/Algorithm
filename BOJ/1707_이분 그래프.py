import sys
sys.setrecursionlimit(10**9)

def dfs(v, group):
    global bipatite

    # 이분 탐색이 아니라면 리턴
    if not bipatite:
        return
    
    # V정점을 첫 번째 그룹으로 등록
    visited[v] = group
    for i in graph[v]:
        # V정점과 인접한 i정점이 방문 상태가 아니라면 dfs함수 호출
        if not visited[i]:
            # 인접 정점은 두 번째 그룹으로 등록
            dfs(i, -group)
        # V정점과 인접한 i정점이 같은 그룹이라면 이분 그래프가 아니므로 False값 리턴
        elif visited[i] == visited[v]:
            bipatite =  False
            return

if __name__ == "__main__":
    K = int(sys.stdin.readline())

    for _ in range(K):
        V, E = map(int, sys.stdin.readline().split())
        graph = [[] for _ in range(V + 1)]
        visited = [False] * (V + 1)
        # 이분 그래프인지 확인하기 위한 플래그 변수(True : 이분 그래프 O, False : 이분 그래프 X)
        bipatite = True
        
        for _ in range(E):
            a, b = map(int, sys.stdin.readline().split())
            graph[a].append(b)
            graph[b].append(a)

        # 정점 1부터 V정점까지 방문 처리가 되어있지 않다면 dfs함수 호출
        for i in range(1, V + 1):
            if visited[i] == False:
                dfs(i, 1)
                # 만약 이분 그래프가 아니라면 반복문 탈출
                if not bipatite:
                    break

        print('YES' if bipatite else 'NO')