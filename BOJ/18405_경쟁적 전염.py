import sys
from collections import deque

def BFS():
    # 바이러스 정보 리스트를 통해 큐 생성
    queue = deque(virus)
    # 몇 초 실행했는지 확인하기 위한 카운트 변수
    cnt = 0
    # 큐가 비어있지 않을 때까지 반복문 수행
    while queue:
        # 카운트가 입력한 초와 같다면 반복문 탈출
        if cnt == s:
            break
        # 큐에 삽입된 바이러스 개수만큼 반복문 수행
        for _ in range(len(queue)):
            # 큐에서 가장 작은 번호인 바이러스 번호와 좌표 삭제
            v_num, v_num_x, v_num_y = queue.popleft()
            # 상하좌우 탐색
            for j in range(4):
                nx = dx[j] + v_num_x
                ny = dy[j] + v_num_y
                # 시험관 범위 안에 있고, 값이 0이면 값을 현재 바이러스 번호로 바꾸고 큐에 삽입
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                    graph[nx][ny] = v_num
                    queue.append((graph[nx][ny], nx, ny))
        # 큐에 삽입된 바이러스 개수만큼 반복문을 모두 수행했다면 카운트 1증가
        
        cnt += 1
    # 결과값 출력
    print(graph[x - 1][y - 1])

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 시험관 크기 N, 바이러스 번호 K 입력
    n, k = map(int, sys.stdin.readline().split())
    # 시험관 정보 빈 리스트
    graph = []
    #바이러스 정보 빈 리스트
    virus = []
    
    # N 줄에 걸쳐서 시험관 정보를 입력하고, 바이러스 정보를 바이러스 리스트에 삽입
    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
        for j in range(n):
            if graph[i][j] != 0:
                virus.append((graph[i][j], i, j))

    # 번호가 낮은 종류의 바이러스부터 먼저 증식하기 때문에 바이러스 정보가 들어간 리스트 정렬
    virus.sort()

    # 초 S, 찾고자 하는 바이러스 좌표 입력            
    s, x, y = map(int, sys.stdin.readline().split())

    # 상하좌우 방향 정보
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS 알고리즘 수행
    BFS()