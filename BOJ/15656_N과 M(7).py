import sys

def DFS():
    if len(S) == M:
        print(*S)
        return
    
    for i in range(1, N + 1):
        S.append(N_List[i - 1])
        DFS()
        S.pop()

N, M = map(int, sys.stdin.readline().split())
N_List = list(map(int, sys.stdin.readline().split()))
N_List.sort()
S = []
DFS()