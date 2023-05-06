# 일반적으로 생각한 풀이
import sys

def solve():
    result = 0
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            result += arr[i][j]
    print(result)

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    for _ in range(M):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        solve()

# 다이나믹 프로그래밍 + 누적합을 이용한 풀이
import sys

def prefix_sum():
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            DP[i][j] = arr[i - 1][j - 1] + DP[i - 1][j] + DP[i][j - 1] - DP[i - 1][j - 1]
    
def range_sum():
    result = DP[x2][y2] - DP[x1 - 1][y2] - DP[x2][y1 - 1] + DP[x1 - 1][y1 - 1]
    print(result)

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    DP = [[0] * (N + 1) for _ in range(N + 1)]
    prefix_sum()

    for _ in range(M):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        result = 0
        range_sum()