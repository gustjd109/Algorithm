import heapq
import sys
input = sys.stdin.readline
# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

def dijkstra(black_room_cnt, x, y):
        q = []
        # 큐에 시작방에서의 흰방으로 바꾸어야 할 최소의 검은 방의 수와 시작방 좌표 삽입
        heapq.heappush(q, [black_room_cnt, x, y])
        distance[x][y] = black_room_cnt
        # 큐가 비어있지 않다면
        while q:
            # 현재 큐에 들어가있는 검은 방의 수와 x, y좌표 꺼내기
            black_room_cnt, x, y = heapq.heappop(q)

            # 불필요한 중복 연산을 허용하지 않게 하기 위해서 현재 검은 방의 수가 현재 방의 검은 방 수보다 크면 무시
            if black_room_cnt > distance[x][y]:
                continue
            
            # x, y 좌표가 N X N 좌표라면 검은 방의 수 반환
            if x == N - 1 and y == N - 1:
                return result
            
            # 상하좌우 탐색 시작
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # nx, ny 좌표가 N X N 좌표를 넘어가지 않으면
                if 0 <= nx < N and 0 <= ny < N:
                    # 결과값에 최소 검은 방의 수 삽입
                    result = black_room_cnt
                    # nx, ny좌표 방이 검은 방이면 결과값 +1
                    if roomboard[nx][ny] == 0:
                        result += 1
                    # nx, ny 좌표의 검은 방 수가 결과값보다 크면 값 바꾸고, 큐에 삽입
                    if result < distance[nx][ny]:
                        distance[nx][ny] = result
                        heapq.heappush(q, [result, nx, ny])

if __name__ == "__main__":
    # 백준 문제의 예제를 txt 파일에 미리 저장해놓고, 매번 복사 과정이 필요없이 바로 출력 가능할 수 있도록 해줌
    sys.stdin = open("input.txt","rt")

    # 한 줄에 들어가는 방의 수 N 입력
    N = int(sys.stdin.readline())
    # N개 줄의 각 줄마다 0과 1이 이루어진 길이가 N인 수열 입력
    roomboard = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]

    # 방향 정보(상하좌우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 다익스트라 알고리즘을 수행
    # 매개변수로 흰방으로 바꾸어야 할 최소의 검은 방의 수와 시작방의 좌표 전달
    print(dijkstra(0, 0, 0))