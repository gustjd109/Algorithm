import sys

def DP():
    # 대각선은 자기 자신이므로 계산 안하고 값을 0으로 유지하기 위해 i값을 1 ~ N으로 설정
    for i in range(1, N):
        # 반복문이 지속되면서 계산 횟수가 N - 1로 감소하므로 j값을 0 ~ N - i로 설정
        for j in range(0, N - i):
            # 대각선 다음 칸부터 계산하기 위해 x값을 i + j로 설정
            x = i + j
            # min 연산을 위해 최대값 미리 할당
            dp[j][x] = 2 ** 32
            # 어떤 행렬로 시작해서 어떤 행렬까지의 곱셈하는 모든 방법의 수만큼 반복문 수행
            for k in range(j, x):
                # 경우의 수만큼 계산된 연산 횟수 값들 중에서 최소 연산 횟수 값을 할당
                dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + M[j][0] * M[k][1] * M[x][1])
    # 최종적으로 구해야할 dp테이블의 0번째 줄의 마지막 값 반환
    print(dp[0][-1])

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 행렬의 개수 N 입력
    N = int(sys.stdin.readline())
    # N개의 행렬 크기 r과 c 입력
    M = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # i번째 앞의 숫자로 시작해서 j번째 뒤의 숫자로 끝나는 행렬의 연산 횟수가 저장되는 dp테이블 초기화
    dp = [[0] * N for _ in range(N)]
    DP()