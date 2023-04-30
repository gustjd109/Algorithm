import sys

def DFS():
    if len(S) == M:
        print(*S)
        return
    
    for i in range(1, N + 1):
        # if visited[i]:
        #     continue

        visited[i] = True
        S.append(i)
        DFS()
        S.pop()
        visited[i] = False

N, M = map(int, sys.stdin.readline().split())
S = []
visited = [False] * (N + 1)
DFS()

# 해당 문제는 중복을 허용하는 문제
# for문 안에 있는 중복 방지를 위해 사용된 if문이 없어도 된다.