import sys

def DFS(start):
    if len(S) == M:
        print(*S)
        return
    
    for i in range(start, N + 1):
        if N_List[i - 1] in S:
            continue

        S.append(N_List[i - 1])
        DFS(i + 1)
        S.pop()

N, M = map(int, sys.stdin.readline().split())
N_List = list(map(int, sys.stdin.readline().split()))
N_List.sort()
S = []
DFS(1)