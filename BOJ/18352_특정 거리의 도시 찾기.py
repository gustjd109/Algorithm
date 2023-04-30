from collections import deque
import sys

def bfs(X):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    # 큐에 출발 도시 X값 삽입
    queue.append(X)

    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 도시 하나 삭제
        X = queue.popleft()

        # 출발한 도시에서 갈 수 있는 인접 도시 탐색
        for city_num in graph[X]:
            # 아직 방문하지 않은 도시라면 최단 거리를 갱신하고 큐에 해당 도시를 삽입
            if distance[city_num] == -1:
                distance[city_num] = distance[X] + 1
                queue.append(city_num)

    # 최단 거리가 K인 도시 존재 유무 확인 플래그 False로 초기화
    have_shortest_city = False
    # 최단 거리가 K인 도시의 번호를 오름차순으로 출력
    for i in range(N + 1):
        if distance[i] == K:
            print(i)
            # 최단 거리가 K인 도시가 있다면 플래그 True로 갱신
            have_shortest_city = True
            
    # 최단 거리가 K인 도시가 없다면 -1 출력
    if have_shortest_city == False:
        print(-1)

if __name__ == "__main__":
    # 도시의 개수 N / 도로의 개수 M / 최단 거리 K / 출발 도시 번호 X 입력
    N, M, K, X = map(int, sys.stdin.readline().split())
    # A번 도시에서 B번 도시로 이동하는 단방향 도로를 저장할 빈 공간
    graph = [[] for _ in range(N + 1)]
    # A번 도시에서 B번 도시로 이동하는 단방향 도로 삽입
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].append(B)
    # 모든 도시의 최단 거리 초기화
    distance = [-1] * (N + 1)
    # 출발 도시 X에서 출발 도시 X로 가는 최단거리는 항상 0이므로 0으로 초기화
    distance[X] = 0

    bfs(X)