import sys
from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

if __name__ == "__main__":
    n, m, v = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        edgeA, edgeB = map(int, sys.stdin.readline().split())
        graph[edgeA].append(edgeB)
        graph[edgeB].append(edgeA)

    # 여러 개의 간선이 있을 경우, 작은 것부터 탐색해야하므로 오름차순으로 정렬
    for i in range(1, n + 1):
        graph[i].sort()

    visited = [False] * (n + 1)
    dfs(v)
    print()
    visited = [False] * (n + 1)
    bfs(v)
    print()