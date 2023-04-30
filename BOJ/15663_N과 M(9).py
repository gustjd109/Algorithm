import sys

def DFS():
    if len(S) == M:
        print(*S)
        return
    
    Tmp_List = 0
    for i in range(len(N_List)):
        if not Visited[i] and Tmp_List != N_List[i]:
            Visited[i] = True
            S.append(N_List[i])
            Tmp_List = N_List[i]
            DFS()
            S.pop()
            Visited[i] = False

N, M = map(int, sys.stdin.readline().split())
N_List = list(map(int, sys.stdin.readline().split()))
N_List.sort()
S = []
Visited = [False] * N
DFS()