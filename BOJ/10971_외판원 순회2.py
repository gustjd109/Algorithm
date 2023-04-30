import sys

def solve(start, cur, cost):
    global answer 
    if start == cur and all(visited): # 시작점과 현재위치가 같고(순회를 마치고 시작점으로 돌아온 상태), 방문 체크 리스트가 모두 방문한 상태일 떄
        answer = min(answer, cost) # 결과값 변수에 결과값과 방문 완료한 후의 비용을 비교하여 더 작은 값을 리턴
        # print(test_list, cost)
        return
    
    for i in range(n): # 0 ~ n - 1번 반복문 수행
        if not w[cur][i] == 0 and not visited[i]: # 현재 위치의 값이 0이 아니고(즉, 같은 도시를 방문하지 않아야 하기 때문), 방문한 상태가 아닐 때
            visited[i] = True # 해당 도시를 방문 처리
            # test_list.append(w[cur][i])
            solve(start, i, cost + w[cur][i]) # 재귀함수 호출(매개변수로 시작점, 방문한 도시 번호, 현재 비용값에 방문한 도시까지의 길이를 더한 값을 전달)
            visited[i] = False # 하나의 재귀함수를 모두 수행하면, 방문한 도시를 방문하지 않은 상태로 처리
            # test_list.pop()

n = int(sys.stdin.readline())
w = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = sys.maxsize
visited = [False] * n
# test_list = []
solve(0, 0, 0) # 매개변수로 시작점, 현재위치, 비용값을 전달
print(answer)