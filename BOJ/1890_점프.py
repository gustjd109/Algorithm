import sys

def find_route_cnt():
    # (0, 0)에서 시작해서 (N - 1, N - 1)까지 가는 경우의 수를 저장할 dp리스트 0으로 초기화
    dp = [[0] * N for _ in range(N)]
    # dp리스트에서 (0, 0)값 1로 초기화
    dp[0][0] = 1

    # (0, 0)에서 (N - 1, N - 1)까지 탐색
    for i in range(N):
        for j in range(N):
            # 현재 위치한 곳이 (N - 1, N - 1)이라면, 더 이상 진행할 수 없는 종착점이므로 (N - 1, N - 1)칸까지 오는 경우의 수 출력
            if i == N - 1 and j == N - 1:
                print(dp[i][j])
                break

            # 현재 위치에서 점프할 수 있는 칸의 값 할당
            cur = game_map[i][j]

            # 아래로 가는 경우
            if i + cur < N:
                # dp리스트에서 아래로 점프한 위치의 값에 현재 칸까지 오는 경우의 수만큼 증가
                dp[i + cur][j] += dp[i][j]

            # 오른쪽으로 가는 경우
            if j + cur < N:
                # dp리스트에서 오른쪽으로 점프한 위치의 값에 현재 칸까지 오는 경우의 수만큼 증가
                dp[i][j + cur] += dp[i][j]


if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 게임 판의 크기 입력
    N = int(sys.stdin.readline())
    # 게임 판의 크기만큼 점프할 수 있는 수 입력
    game_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 갈 수 있는 경로 찾기 함수 수행
    find_route_cnt()