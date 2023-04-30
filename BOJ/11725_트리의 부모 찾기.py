import sys
sys.setrecursionlimit(10**9)

def dfs(i):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(j)
            parent[j] = i

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    parent = [0] * (N + 1)
    
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N + 1):
        graph[i].sort()

    dfs(1)

    for i in range(2, N + 1):
        print(parent[i])