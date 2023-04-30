import sys

def DFS():
    if len(S) == M:
        print(*S)
        return
    
    for i in range(1, N + 1):
        if N_List[i - 1] in S: # 중복 방지를 위해 N_List[i]값이 S리스트에 있으면 건너뜀 
            continue

        S.append(N_List[i - 1])
        DFS()
        S.pop()

N, M = map(int, sys.stdin.readline().split())
N_List = list(map(int, sys.stdin.readline().split()))
N_List.sort() # 출력값을 보면 값이 입력된 순서가 아닌, 정렬된 순서로 출력되는 것을 확인할 수 있다.
S = []
DFS()