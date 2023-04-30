import sys

def DFS(start):
    if len(S) == M:
        print(*S)
        return
    
    for i in range(start, N + 1):
        visited[i] = True
        S.append(i)
        DFS(i) # 중복을 허용하기 위해 i값을 넘겨준다.
        S.pop()
        visited[i] = False

N, M = map(int, sys.stdin.readline().split())
S = []
visited = [False] * (N + 1)
DFS(1)

# 비내림차순이란, 각각의 원소가 바로 앞에 있는 원소보다 크거나 같을 경우를 말한다.
# 만약 그러한 수열이 여러개라면 사전순으로 앞서는 것을 출력한다.