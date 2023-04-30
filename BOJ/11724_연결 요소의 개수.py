import sys
sys.setrecursionlimit(10**9)

def dfs(i):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(j)

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    cnt = 0
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        if not visited[i]:
            cnt += 1
            dfs(i)

    print(cnt)