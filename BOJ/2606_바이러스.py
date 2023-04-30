import sys
sys.setrecursionlimit(10**9)

def dfs(i):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(j)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    e = int(sys.stdin.readline())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1)
    print(sum(visited) - 1)