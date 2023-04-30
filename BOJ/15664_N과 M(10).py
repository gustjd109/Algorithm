import sys

def DFS(start):
    if len(S) == M:
        print(*S)
        return
    
    Tmp = 0
    for i in range(start, N):
        if not Visited[i] and N_List[i] != Tmp:
            Visited[i] = True
            S.append(N_List[i])
            Tmp = N_List[i]
            DFS(i + 1)
            S.pop()
            Visited[i] = False

N, M = map(int, sys.stdin.readline().split())
N_List = sorted(list(map(int, sys.stdin.readline().split())))
S = []
Visited = [False] * N
DFS(0)