import heapq
import sys
# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

def dijkstra(start):
        q = []
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
        heapq.heappush(q, (0, start))
        distance[start] = 0
         # 큐가 비어있지 않다면
        while q:
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[now] < dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 도시 개수 입력
    N = int(sys.stdin.readline())
    # 버스 대수 입력
    M = int(sys.stdin.readline())
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
    graph = [[] for _ in range(N + 1)]
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (N + 1)

    # 모든 간선 정보를 입력받기
    for _ in range(M):
        start_city, end_city, start_end_cost = map(int, input().split())
        # 시작 도시에서 도착 도시로 가는 비용 리스트에 저장
        graph[start_city].append((end_city, start_end_cost))
    
    # 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호 입력
    start, end = map(int, sys.stdin.readline().split())

    # 다익스트라 알고리즘을 수행
    dijkstra(start)

    # 구하고자 하는 구간인 출발점의 도시에서부터 도착점의 도시까지의 최단 거리 출력
    print(distance[end])