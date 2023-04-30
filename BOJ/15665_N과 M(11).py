import sys

def DFS():
    if len(S) == M:
        print(*S)
        return
    
    Tmp = 0
    for i in range(N):
        if N_List[i] != Tmp:
            S.append(N_List[i])
            Tmp = N_List[i]
            DFS()
            S.pop()

N, M = map(int, sys.stdin.readline().split())
N_List = sorted(list(map(int, sys.stdin.readline().split())))
S = []
Visited = [False] * N
DFS()